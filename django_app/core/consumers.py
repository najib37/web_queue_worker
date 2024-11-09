import json
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import aio_pika

amqp_url = 'amqp://userf:userd@rabbitmq:5672'
exchange_name = 'progress_exchange'
queue_name = 'progress_queue'
routing_key = 'progress'

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.consumer = asyncio.create_task(self.rabbit_connection())

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        await self.send(text_data=json.dumps({"message": message}))

    async def send_message(self, message):
        await self.send(text_data=json.dumps(message))

    async def process_message(self, message: aio_pika.abc.AbstractIncomingMessage) -> None:
        async with message.process():
            await self.send_message(json.loads(message.body.decode()))

    async def rabbit_connection(self) -> None:
        connection = await aio_pika.connect_robust(amqp_url)
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=100)
        exchange = await channel.declare_exchange(
            exchange_name,
            aio_pika.ExchangeType.DIRECT,
            durable=True
        )

        queue = await channel.declare_queue(queue_name, durable=True)
        await queue.bind(exchange, routing_key)
        await queue.consume(lambda message: self.process_message(message))
        try:
            await asyncio.Future()
        finally:
            await connection.close()

