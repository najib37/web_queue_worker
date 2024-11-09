from kombu import Connection, Exchange, Queue, Consumer

class RabbitMQConsumer:
    def __init__(self, amqp_url, exchange_name, queue_name, routing_key):
        self.exchange = Exchange(exchange_name, type='direct')
        self.queue = Queue(name=queue_name, exchange=self.exchange, routing_key=routing_key)
        self.connection = Connection(amqp_url)
        self.connection.connect()

    def process_message(self, body, message):
        print(f"Received message: {body}")
        message.ack()

    def start_consuming(self):
        print("Starting consumer...")
        consumer = Consumer(self.connection, queues=[self.queue], callbacks=[self.process_message], accept=['json'])
        consumer.consume()
        self.connection.drain_events()

def run_consumer():
    amqp_url = 'amqp://userf:userd@rabbitmq:5672'
    exchange_name = 'progress_exchange'
    queue_name = 'progress_queue'
    routing_key = 'progress'
    
    consumer = RabbitMQConsumer(amqp_url, exchange_name, queue_name, routing_key)
    consumer.start_consuming()

run_consumer()

