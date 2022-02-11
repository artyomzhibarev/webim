import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings


class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.val = 0

    def set(self, new_value):
        self.val = new_value

    def get(self):
        return self.val


singleton_1 = Singleton()


class RandomNumberConsumer(AsyncWebsocketConsumer):
    group_name = settings.STREAM_SOCKET_GROUP_NAME

    async def connect(self):
        # Joining group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive data from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # print(message)
        # Print message that receive from Websocket

        # Send data to group

        # print(f'From consumers: {singleton}')
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'random_num',
                'data': {
                    'random_number': singleton_1.get()
                }
            }
        )

    async def random_num(self, event):
        # Receive data from group
        await self.send(text_data=json.dumps(event['data']))
