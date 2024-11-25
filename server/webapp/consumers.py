import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import uuid

from gpt4all import GPT4All
from django.conf import settings

from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "chat_room"
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
    
    def disconnect(self, close_code):
        # Leave room group
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    def receive(self, text_data):
        event = json.loads(text_data)
        inputMessage = event['inputMessage']
        id = str(uuid.uuid4())

        async_to_sync(
            self.send(text_data=json.dumps({
                'type': 'initiateDialog',
                'inputMessage': inputMessage,
                'id': id,
            }))
        )

        for chunk in self.streamResponse(inputMessage):
            async_to_sync(
                self.send(text_data=json.dumps({
                    'type': 'token',
                    'token': chunk,
                    'id': id,
                }))
            )
        


    def streamResponse(self, inputMessage):
        model = GPT4All(str(settings.MODEL_PATH))
        generator = model.generate(inputMessage, streaming=True)
        for chunk in generator:
            yield chunk

"""
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "chat_room"
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Print the received message in the Django server
        data = json.loads(text_data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'inputMessage': data['inputMessage'],
                'id': str(uuid.uuid4()),
            }
        )

    async def chat_message(self, event):
        inputMessage, id = event['inputMessage'], event['id']        
        await self.send(text_data=json.dumps({
            'type': 'initiateDialog',
            'inputMessage': inputMessage,
            'id': id,
        }))
        
        async for chunk in self.streamResponse(inputMessage):
            await self.send(text_data=json.dumps({
                'type': 'token',
                'token': chunk,
                'id': id,
            }))

    async def streamResponse(self, inputMessage):
        model = GPT4All(str(settings.MODEL_PATH))
        generator = model.generate(inputMessage, streaming=True)
        for chunk in generator:
            yield chunk
"""