
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django_tasks import task


# @task()
def websocket_group_send(room_name: str, message: dict):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_name,
        {
            'type': 'chat.message',
            'message': message
        }
    )
