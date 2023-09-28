import json
import logging
import uuid
from twisted.web.resource import Resource
from twisted.web.server import Request
from twisted.web import http
from synapse.module_api import ModuleApi
from synapse.logging.context import run_in_background
import base64
"""Usage

    curl --location --request POST 'http://localhost:8008/_synapse/client/demo/scheduled-message' \
--header 'Content-Type: application/json' \
--data '{
    "message": "hello, world!",
    "room_id": "!<room_id>:matrix.lab-lama.com",
    "timestamp": "1695803171"
}'
"""

logger = logging.getLogger(__name__)


class ScheduledMessageResource(Resource):
    def __init__(self, config, hs, api):
        super(ScheduledMessageResource, self).__init__()
        self.config = config
        self.hs = hs
        self.api = api
        self.auth = self.hs.get_auth()
        self.store = hs.get_datastores().main
        self.clock = hs.get_clock()

    def render_POST(self, request: Request):
        json_obj = json.loads(request.content.read())
        self.message = (json_obj["message"])
        self.room_id = (json_obj["room_id"])
        self.timestamp = (json_obj["timestamp"])

        # TODO: extract token and validate it
        authorization_header = request.requestHeaders.getRawHeaders(
            b'Authorization', [b''])[0].decode('utf-8')
        # Split the apikey_header into parts
        parts = authorization_header.split()

        if len(parts) == 2 and parts[0] == 'Bearer':
            # The first part is 'Bearer', extract the syt_YWRtaW4_WejdMmSNPFapoGhaUVfJ_3nraJw espcially YWRtaW4 because it's base64(user_id)
            access_token = parts[1]
            # Extract the value between the underscores
            underscore_parts = access_token.split('_')
            if len(underscore_parts) >= 3:
                user_id = underscore_parts[1]
                # Add padding characters if necessary
                user_id += '=' * ((4 - len(user_id) % 4) % 4)
                user_id = base64.b64decode(user_id).decode('utf-8')
                sender = self.api.get_qualified_user_id(user_id)

        # TODO: check if the user_id has a membership in the room

        # run_in_background(self.process_request,
        #                   self.message, self.room_id, self.timestamp, sender)

        request.setResponseCode(http.CREATED)
        request.setHeader(b"content-type", b"application/json")
        request.setHeader(b"content-length", b"0")
        # returning b"" because twisted only allows byte type of return and the return is manadtory
        return b""

    async def process_request(self, message, room_id, timestamp, sender):
        # synapse/storage/databases/main/scheduled_message.py
        # generate new request_id
        request_id = str(uuid.uuid4())
        await self.store.insert_scheduled_message_request(request_id, message, room_id, timestamp, sender)
        # synapse/replication/tcp/handler.py
        # TODO: this send message handler has to be invoked from different place
        # and it must be automatically instead of hardcoding them
        # TODO: in this example i sent one scheduled message but it should be there a
        # query to get all the messages with timestamp past the current timestamp
        self.hs.get_replication_command_handler().send_scheduled_message(request_id)


class ScheduledMessage:
    def __init__(self, config: dict, api: ModuleApi):
        self.config = config
        self.api = api
        self.hs = api._hs

        # logger.warning(self.hs._instance_name)
        # logger.warning(self.hs.get_room_member_handler().member_linearizer)

        self.api.register_web_resource(
            path="/_synapse/client/demo/scheduled-message",
            resource=ScheduledMessageResource(self.config, self.hs, self.api)
        )

    @staticmethod
    def parse_config(config):
        return config
