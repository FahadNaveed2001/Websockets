from django.urls import path
from myproject.consumers import StatusConsumer

websocket_urlpatterns = [
    path('ws/status/', StatusConsumer.as_asgi()),
]
