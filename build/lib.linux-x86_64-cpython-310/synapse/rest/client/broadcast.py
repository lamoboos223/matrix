from synapse.http.server import HttpServer
from synapse.http.site import SynapseRequest

from typing import Tuple
from synapse.types import JsonDict, Requester

from twisted.web.server import Request

from synapse.http.servlet import (
    RestServlet,
    parse_json_object_from_request
)

from synapse.rest.client._base import client_patterns

from http import HTTPStatus

import uuid

from synapse.logging.context import run_in_background
from twk.broadcast import BroadcastRuntimeService


class BroadcastRestServlet(RestServlet):
    # No PATTERN; we have custom dispatch rules here

    def __init__(self, hs: "HomeServer"):
        super().__init__()
        self.hs = hs
        self.store = hs.get_datastores().main
        self.clock = hs.get_clock()
        self.auth = hs.get_auth()

    def register(self, http_server: HttpServer) -> None:
        PATTERNS = "/broadcast"
        register_txn_path(self, PATTERNS, http_server)

    async def process_broadcast_request(self, request_id, broadcaster_id,
                                        topics, access_token_id, message):
        # Insert a new request into the request table
        # (request_id, broadcaster_id, topics, message)
        await self.store.insert_broadcast_request(request_id, broadcaster_id,
                                                  topics,
                                                  message,
                                                  int(self.clock.time_msec()))

        # Fetch data from MSSQL UserTopics table then add to
        # the runtime table 'broadcast_request_message_delivery'
        brs = BroadcastRuntimeService(self.hs)
        await brs.queue_request_items(request_id, broadcaster_id, topics,
                                      access_token_id)

    async def on_POST(self, request: SynapseRequest) -> Tuple[int, JsonDict]:
        requester = await self.auth.get_user_by_req(request)

        return await self._do(request, requester)

    async def _do(
        self, request: SynapseRequest, requester: Requester
    ) -> Tuple[int, JsonDict]:
        # generate new request_id
        request_id = str(uuid.uuid4())

        broadcaster_id = requester.user.to_string()
        broadcaster_access_token_id = requester.access_token_id

        broadcast_details = self.get_broadcast_details(request)

        topics = broadcast_details.get("topics")
        topics = topics.replace(" ", "")  # remove spaces

        message = broadcast_details.get("message")

        run_in_background(self.process_broadcast_request,
                          request_id,
                          broadcaster_id,
                          topics,
                          broadcaster_access_token_id,
                          message)

        # Request accepted, processing continues off-line
        return HTTPStatus.ACCEPTED, {"request_id": request_id}

    def get_broadcast_details(self, request: Request) -> JsonDict:
        broadcast_details = parse_json_object_from_request(request)
        return broadcast_details


def register_txn_path(
    servlet: RestServlet,
    regex_string: str,
    http_server: HttpServer,
) -> None:
    """Registers a transaction-based path.

    This registers two paths:
        PUT regex_string/$txnid
        POST regex_string

    Args:
        regex_string: The regex string to register. Must NOT have a
            trailing $ as this string will be appended to.
        http_server: The http_server to register paths with.
    """
    on_POST = getattr(servlet, "on_POST", None)
    if on_POST is None:
        raise RuntimeError("on_POST must exist when using register_txn_path")
    http_server.register_paths(
        "POST",
        client_patterns(regex_string + "$", v1=True),
        on_POST,
        servlet.__class__.__name__,
    )


def register_servlets(hs: "HomeServer", http_server: HttpServer) -> None:
    BroadcastRestServlet(hs).register(http_server)
