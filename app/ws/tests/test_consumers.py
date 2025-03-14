
import pytest
from channels_redis.core import RedisChannelLayer
from faker import Faker
from websockets.asyncio import async_timeout

from app.ws.tests.conftest import REDIS_TEST_HOSTS

fake = Faker()


class TestUploadingLogsConsumer:

    @pytest.mark.asyncio
    async def test_websocket_connection(self, ws_communicator):
        connected, subprotocol = await ws_communicator.connect()
        assert connected
        assert subprotocol is None

    @pytest.mark.asyncio
    async def test_sending_json(self, ws_communicator):
        await ws_communicator.send_json_to({"hello": "world"})
        response = await ws_communicator.receive_json_from()
        assert response == {"hello": "world"}

    @pytest.mark.asyncio
    async def test_layer_send_receive(self):
        channel_layer = RedisChannelLayer(hosts=REDIS_TEST_HOSTS)
        message = {
            'type': 'chat.message',
            'message': 'message'
        }
        await channel_layer.send(
            "uploading_logs_channel",
            message
        )

        receive_msg = await channel_layer.receive("uploading_logs_channel")
        assert receive_msg['type'] == message['type']
        assert receive_msg['message'] == message['message']

        await channel_layer.flush()

    @pytest.mark.asyncio
    async def test_layer_group_send(self):
        channel_layer = RedisChannelLayer(hosts=REDIS_TEST_HOSTS)
        test_group_name = 'uploading_logs_channel'
        message = {
            'type': 'chat.message',
            'message': fake.text(max_nb_chars=20)
        }

        channel_name1 = await channel_layer.new_channel(prefix="test-gr-chan-1")
        channel_name2 = await channel_layer.new_channel(prefix="test-gr-chan-2")

        await channel_layer.group_add(test_group_name, channel_name1)
        await channel_layer.group_add(test_group_name, channel_name2)

        await channel_layer.group_send(test_group_name, message)

        async with async_timeout.timeout(1):
            assert (await channel_layer.receive(channel_name1))["message"] == message['message']
            assert (await channel_layer.receive(channel_name2))["message"] == message['message']

        await channel_layer.flush()
