# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(
        r"ws/btcusdt/",
        consumers.ProgressBarConsumer.as_asgi(),
    ),
]
