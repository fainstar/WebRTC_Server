import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import ChatConsumer

# 設定 Django 的環境變數
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebSocket_Server.settings')

# 路由設定：告訴 ASGI 如何處理各種協議（HTTP、WebSocket 等）
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # 傳統 HTTP 請求使用 Django 的預設 WSGI 應用
    "websocket": AuthMiddlewareStack(  # WebSocket 需要通過身份認證
        URLRouter([
            path('ws/mode/', ChatConsumer.as_asgi()),  # 設定 WebSocket 路由
        ])
    ),
})
