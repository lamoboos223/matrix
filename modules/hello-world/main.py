import json

from twisted.web.resource import Resource
from twisted.web.server import Request

from synapse.module_api import ModuleApi

"""Usage

    curl --location --request GET 'http://localhost:8008/_synapse/client/demo/hello' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Lama"
}'
"""


class HelloWorldResource(Resource):
    def __init__(self, config):
        """This is a hello world web resource served by the synpase homeserver with the path given to ModuleApi object

        Args:
            config (dict): it is a dictionary for the config object in the homeserver.yaml this is the full directive modules.module.config
        """
        super(HelloWorldResource, self).__init__()
        self.config = config

    def render_GET(self, request: Request):
        # if the name is query string
        # name = request.args.get(b"name")[0].decode("utf-8")

        # if the name is json payload
        json_obj = json.loads(request.content.read())
        name = (json_obj["name"])

        json_response = {
            "hello": name
        }
        request.setHeader(b"content-type", b"application/json")
        return bytes(json.dumps(json_response), "utf-8")


class HelloWorld:
    def __init__(self, config: dict, api: ModuleApi):
        self.config = config
        self.api = api

        self.api.register_web_resource(
            path="/_synapse/client/demo/hello",
            resource=HelloWorldResource(self.config)
        )

    @staticmethod
    def parse_config(config):
        return config