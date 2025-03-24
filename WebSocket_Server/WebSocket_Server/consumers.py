# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # WebSocket 連接時的邏輯
        self.room_name = 'chat_room'  # 設定聊天房間
        self.room_group_name = f"chat_{self.room_name}"

        # 加入房間
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # 確認連接
        await self.accept()

    async def disconnect(self, close_code):
        # 斷開連接時的邏輯
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # 接收消息並發送給房間中的其他客戶端
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 發送消息到房間組
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # 接收來自房間組的消息並發送給 WebSocket 客戶端
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
