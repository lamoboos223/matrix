from synapse.storage._base import SQLBaseStore
from synapse.storage.database import (
    DatabasePool,
    LoggingDatabaseConnection
)


class BroadcastRequestStore(SQLBaseStore):
    def __init__(
        self,
        database: DatabasePool,
        db_conn: LoggingDatabaseConnection,
        hs: "HomeServer",
    ):
        super().__init__(database, db_conn, hs)

    async def get_request_data(self, request_id):
        return await self.db_pool.simple_select_one(
            "broadcast_requests",
            {
                "request_id": request_id
            },
            ["broadcaster_id", "message"],
            desc="get_request_data"
        )

    async def insert_broadcast_request(self, request_id, broadcaster_id, topics,
                                       message, timestamp):
        await self.db_pool.simple_insert(
            "broadcast_requests",
            {
                "request_id": request_id,
                "broadcaster_id": broadcaster_id,
                "topics": topics,
                "message": message,
                "timestamp": timestamp,
            },
            desc="insert_broadcast_request",
        )

    async def insert_broadcast_request_message_delivery(self, request_id, page, room_id,
                                                        timestamp, hash_total):
        await self.db_pool.simple_insert(
            "broadcast_request_message_delivery",
            {
                "request_id": request_id,
                "page": page,
                "room_id": room_id,
                "timestamp": timestamp,
                "hash_total": hash_total
            },
            desc="insert_broadcast_request_message_delivery",
        )

    async def delete_broadcast_request_message_delivery_for_room(self, request_id,
                                                                 room_id):
        await self.db_pool.simple_delete(
            "broadcast_request_message_delivery",
            {
                "request_id": request_id,
                "room_id": room_id
            },
            desc="delete_broadcast_request_message_delivery_for_room",
        )

    async def get_room_ids_by_request_id(self, request_id, page, num_instances,
                                         instance_idx):
        return await self.db_pool.simple_select_onecol(
            "broadcast_request_message_delivery",
            {
                "request_id": request_id,
                "page": page,
                "hash_total %% " + str(num_instances): instance_idx
            },
            "room_id",
            desc="get_room_ids_by_request_id_for_broadcast"
        )
