import yaml
import re

from twk.db import MSSQLWrapper
from twk.broadcast.constants import BroadcastRuntimeServiceConstants

from synapse.config._base import ShardedWorkerHandlingConfig

import logging

logger = logging.getLogger(__name__)


class BroadcastRuntimeService:

    def __init__(self, hs: "HomeServer"):
        self.hs = hs
        self.store = hs.get_datastores().main
        self.clock = hs.get_clock()

        # Read broadcast source connection string URL data
        with open(BroadcastRuntimeServiceConstants.BROADCAST_SOURCE_CON_YAML_FILE_PATH,
                  'r') as f:
            config = yaml.safe_load(f)

        self.page_size = config['broadcast.source']['page-size']

        server = config['broadcast.source']['server']
        database = config['broadcast.source']['database']
        username = config['broadcast.source']['username']
        password = config['broadcast.source']['password']
        trust_cert = "yes"

        self.mssql = MSSQLWrapper(server=server,
                                  database=database,
                                  username=username,
                                  password=password,
                                  trust_cert=trust_cert)

    async def queue_request_items(self, request_id, broadcaster_id, topics,
                                  access_token_id):
        topic_ids = topics.split(",")

        # 1- Fetch data from MSSQL UserTopics table

        # Convert to int
        for i in range(0, len(topic_ids)):
            topic_ids[i] = int(topic_ids[i])

        page_size = int(self.page_size)  # number of records to fetch per page
        order_by = "NationalId"

        query = """
                SELECT DISTINCT NationalId
                FROM UserTopics
                WHERE {}
            """.format(' OR '.join('TopicId = {}'.format(id) for id in topic_ids))

        total_records = self.mssql.count(f"SELECT COUNT(*) FROM ({query}) t")
        pages = (total_records + page_size - 1) // page_size

        pattern = '@(.*):' + self.hs.hostname
        broadcaster_name = re.search(pattern, broadcaster_id).group(1)

        for page in range(1, pages + 1):

            logger.debug(
                "fetching page: %s",
                page
            )

            rows = self.mssql.execute_query(query, order_by, page_size=page_size,
                                            page=page)
            for row in rows:
                national_id = row.NationalId

                # 2- Add to the runtime table 'broadcast_request_message_delivery'

                room_id = f"!{broadcaster_name}_{national_id}:{self.hs.hostname}"
                ts = int(self.clock.time_msec())
                hash_total = ShardedWorkerHandlingConfig.hash_total(room_id)

                await self.store.insert_broadcast_request_message_delivery(request_id,
                                                                           page,
                                                                           room_id,
                                                                           ts,
                                                                           hash_total)
            # send a BroadcastCommand as per page
            self.hs.get_replication_command_handler().send_broadcast(request_id,
                                                                     page,
                                                                     topics,
                                                                     access_token_id)
