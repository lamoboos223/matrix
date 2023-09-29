import logging
import uuid
from twisted.web.resource import Resource
from twisted.web.server import Request
from twisted.web import http
from synapse.module_api import ModuleApi
from synapse.logging.context import run_in_background
from synapse.api.auth import Auth
from synapse.storage.databases.main import DataStore
from synapse.util import Clock
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
    def __init__(self, config, hs: "HomeServer", api: ModuleApi):
        super(ScheduledMessageResource, self).__init__()
        self.config = config
        self.hs = hs
        self.api = api
        self.auth: Auth = self.hs.get_auth()
        self.store: DataStore = hs.get_datastores().main
        self.clock: Clock = hs.get_clock()

    def render_POST(self, request: Request):
        run_in_background(self.process_request, request)

        request.setResponseCode(http.CREATED)
        request.setHeader(b"content-type", b"application/json")
        request.setHeader(b"content-length", b"0")
        # returning b"" because twisted only allows byte type of return and the return is manadtory
        return b""

    async def process_request(self, request):
        user_requester = await self.auth.get_user_by_req(request=request)
        sender = user_requester.user
        # synapse/storage/databases/main/scheduled_message.py
        request_id = str(uuid.uuid4())
        # check if the requester of scheduling the message in the room
        members = await self.store.get_users_in_room(request.room_id)
        if sender in members:
            await self.store.insert_scheduled_message_request(request_id, request.message, request.room_id, request.timestamp, sender)
        # synapse/replication/tcp/handler.py
        # TODO: this send message handler has to be invoked from different place
        # and it must be automatically instead of hardcoding them
        # TODO: in this example i sent one scheduled message but it should be there a
        # query to get all the messages with timestamp past the current timestamp
        # self.hs.get_replication_command_handler().send_scheduled_message(request_id)


class ScheduledMessage:
    def __init__(self, config: dict, api: ModuleApi):
        self.config = config
        self.api = api
        self.hs = api._hs
        self.api.register_web_resource(
            path="/_synapse/client/demo/scheduled-message",
            resource=ScheduledMessageResource(self.config, self.hs, self.api)
        )

    @staticmethod
    def parse_config(config):
        return config
