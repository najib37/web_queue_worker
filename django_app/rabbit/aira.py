import asyncio
import aio_pika

amqp_url = 'amqp://userf:userd@localhost:5672'
exchange_name = 'progress_exchange'
queue_name = 'progress_queue'
routing_key = 'progress'

async def process_message(
    message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        print(message.body)
        await asyncio.sleep(1)

async def main() -> None:

    print('Connecting to RabbitMQ')
    connection = await aio_pika.connect_robust(amqp_url)

    # Creating channel
    print('Creating channel')
    channel = await connection.channel()

    # Maximum message count which will be processing at the same time.
    
    await channel.set_qos(prefetch_count=100)

    # Declaring exchange
    print('Declaring exchange')
    # exchange = await channel.declare_exchange(exchange_name, aio_pika.ExchangeType.DIRECT)
    exchange = await channel.declare_exchange(exchange_name, aio_pika.ExchangeType.DIRECT, durable=True)

    # Declaring queue
    print('Declaring queue')
    queue = await channel.declare_queue(queue_name, durable=True)

    # Binding queue to exchange with routing key
    print('Binding queue to exchange with routing key')
    await queue.bind(exchange, routing_key)

    print('Start consuming')
    await queue.consume(process_message)

    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await connection.close()

if __name__ == "__main__":
    asyncio.run(main())

