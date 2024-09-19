import json
import asyncio
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.utils.timezone import make_aware
from django.contrib.auth import get_user_model

User = get_user_model()

class StatusConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data):
        data = json.loads(text_data)

        identity = data.get('identity')
        status = data.get('status')

        # Print the received data
        print(f"Data received: Identity - {identity}, Status - {status}")

        # Optionally, send a confirmation message back to the client
        await self.send(text_data=json.dumps({
            'message': 'Data received successfully'
        }))
