import os

import pytest
import pytest_asyncio
from channels.testing import WebsocketCommunicator

from app.ws.tests.factories import ImageFactory
from config.asgi import ws_application

TEST_HOST = 'http://0.0.0.0:80'
REDIS_TEST_HOSTS = [os.getenv('REDIS_URL', default='redis://redis:6379/0')]


@pytest.fixture
def image(db):
    return ImageFactory()


@pytest_asyncio.fixture(scope='function')
async def ws_communicator():
    comm = WebsocketCommunicator(ws_application, "/ws/logs/uploading/")
    yield comm
    await comm.disconnect()
