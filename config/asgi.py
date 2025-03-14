import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from config import websocket_urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

ws_application = URLRouter(websocket_urls.websocket_urlpatterns)

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "https": get_asgi_application(),
        "websocket": ws_application,
    }
)
