from celery import Celery
import csv
import json
from kombu import Connection, Exchange, Queue, Producer


# INFO: this file is just to semulate the converter, it's full of hacks

app = Celery(
    'tasks',
    backend='redis://redis:6379',
    broker="amqp://userf:userd@rabbitmq:5672"
    # TODO: these need to be replaced by env variables 
)

# Kombu setup
exchange = Exchange('progress_exchange', type='direct')
queue = Queue(name='progress_queue', exchange=exchange, routing_key='progress')

@app.task(name='converter')
def converter(filename: str):
    # Kombu connection
    with Connection('amqp://userf:userd@rabbitmq:5672') as conn:
        producer = Producer(conn)
        filename = "./media/" + filename
        jsonFileName = "./media/download.json"

        jsonfile = open(jsonFileName, 'w') 
        jsonfile.write('[\n')
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            total_rows = sum(1 for row in reader)
            csvfile.seek(0)
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                json.dump(row, jsonfile)
                jsonfile.write(',\n')
                progress = (i + 1) / total_rows * 100
                producer.publish(
                    {'progress': progress},
                    exchange=exchange,
                    routing_key='progress',
                    declare=[queue]
                )
        jsonfile.write(']')
        #########################

    return "success"
