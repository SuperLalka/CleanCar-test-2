
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.conf import settings


class UploadingLogsConsumer(AsyncJsonWebsocketConsumer):
    room_name = 'uploading_logs_channel'
    room_group_name = 'uploading_logs_channel'

    async def connect(self):
        self.room_name = settings.CHANNELS['uploading_logs_channel']
        self.room_group_name = self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive_json(self, content, **kwargs):
        await self.send_json(content)

    async def chat_message(self, event):
        message = event['message']
        await self.send_json(message)
