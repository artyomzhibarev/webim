import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from app.redis_server import redis_instance


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
        # number = redis_instance.get('rand_num')
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'random_num',
                'data': {
                    'random_number': int(redis_instance.get('rand_num'))
                }
            }
        )

    async def random_num(self, event):
        # Receive data from group
        await self.send(text_data=json.dumps(event['data']))
