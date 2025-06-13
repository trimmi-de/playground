import json
import random
from asyncio import sleep
from datetime import datetime

from channels.generic.websocket import AsyncWebsocketConsumer


class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Send data every 2 seconds
        while True:
            data = {
                'value': random.randint(1, 100),
                'timestamp': str(datetime.now())
            }
            await self.send(json.dumps(data))
            await sleep(2)

    async def receive(self, text_data=None, bytes_data=None):
        # Handle incoming messages if needed
        pass


    async def disconnect(self, close_code):
        self.keep_sending = False
        await self.close()
