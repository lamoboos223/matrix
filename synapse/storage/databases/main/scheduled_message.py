from synapse.storage._base import SQLBaseStore
from synapse.storage.database import (
    DatabasePool,
    LoggingDatabaseConnection
)


class ScheduledMessageStore(SQLBaseStore):
    def __init__(
        self,
        database: DatabasePool,
        db_conn: LoggingDatabaseConnection,
        hs: "HomeServer",
    ):
        super().__init__(database, db_conn, hs)
        
    async def insert_scheduled_message_request(self, request_id, message, room_id, timestamp):
        await self.db_pool.simple_insert(
            "scheduled_messages",
            {
                "request_id": request_id,
                "message": message,
                "room_id": room_id,
                "timestamp": timestamp,
            },
            desc="insert_scheduled_message_request",
        )


    async def get_scheduled_message_request(self, request_id):
        return await self.db_pool.simple_select_one(
            "scheduled_messages",
            {
                "request_id": request_id
            },
            ["message", "room_id", "timestamp"],
            desc="get_scheduled_message_request"
        )



    async def delete_scheduled_message_request(self, request_id):
        await self.db_pool.simple_delete(
            "scheduled_messages",
            {
                "request_id": request_id
            },
            desc="delete_broadcast_request_message_delivery_for_room",
        )


