import json
import logging
import uuid
from twisted.web.resource import Resource
from twisted.web.server import Request
from twisted.web import http
from synapse.module_api import ModuleApi
from synapse.logging.context import run_in_background
import datetime
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
    def __init__(self, config, hs):
        super(ScheduledMessageResource, self).__init__()
        self.config = config
        self.hs = hs
        self.auth = self.hs.get_auth()
        self.store = hs.get_datastores().main
        self.clock = hs.get_clock()

    def render_POST(self, request: Request):
        json_obj = json.loads(request.content.read())
        self.message = (json_obj["message"])
        self.room_id = (json_obj["room_id"])
        self.timestamp = (json_obj["timestamp"])
        
        run_in_background(self.process_request,
                          self.message, self.room_id, self.timestamp)

        request.setResponseCode(http.CREATED)
        request.setHeader(b"content-type", b"application/json")
        request.setHeader(b"content-length", b"0")
        # returning b"" because twisted only allows byte type of return and the return is manadtory
        return b""
    
    async def process_request(self, message, room_id, timestamp):
        # synapse/storage/databases/main/scheduled_message.py
        # generate new request_id
        request_id = str(uuid.uuid4())
        await self.store.insert_scheduled_message_request(request_id, message, room_id, timestamp) 
        
        self.hs.get_replication_command_handler().send_scheduled_message(request_id, message, room_id, timestamp)
    
        



class ScheduledMessage:
    def __init__(self, config: dict, api: ModuleApi):
        self.config = config
        self.api = api
        self.hs = api._hs

        # logger.warning(self.hs._instance_name)

        self.api.register_web_resource(
            path="/_synapse/client/demo/scheduled-message",
            resource=ScheduledMessageResource(self.config, self.hs)
        )

    @staticmethod
    def parse_config(config):
        return config