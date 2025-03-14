
from django.urls import re_path

from app.ws import consumers

websocket_urlpatterns = [
    re_path(r"ws/logs/uploading/$", consumers.UploadingLogsConsumer.as_asgi()),
]
