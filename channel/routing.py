from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('room', consumers.ChatConsumer.as_asgi()),
]