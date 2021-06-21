
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls  import path
from Neuro_channels import consumer
from channels.auth import AuthMiddlewareStack

websocket_urlPattern=[
    path('ws/polData/',consumer.DashConsumer.as_asgi()),
]
application=ProtocolTypeRouter({
    # 'http':
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))

})


