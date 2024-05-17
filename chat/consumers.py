import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from channelsWS.cls.state import State
from chat.models import ConnectedUsers


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('connected: %s' % self.scope['user'])
        self.accept()

    def disconnect(self, close_code):
        print('disconnected')

    # Receive message from WebSocket
    def receive(self, text_data):
        print('receive: %s' % text_data)
        # # send to the client
        self.send('The data is %s received at the server side!' % text_data)

        value = text_data
        result = int(value) * 2
        self.send(text_data=str(result))

    # Receive message from room group
    def chat_message(self, event):
        pass
