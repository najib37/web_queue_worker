
from celery import Celery
from pathlib import Path
import csv
import json

BASEDIR = Path(__file__).resolve().parent.parent

app = Celery (
    'tasks',
    backend='redis://redis:6379',
    broker="amqp://userf:userd@rabbitmq:5672"
    # TODO: these needs to be replaced by env variables 
)

@app.task(name='converter')
def converter(filename):
    jsonfile = open('test.json', 'w') 

    # some hacks but the point is to iterate on the data and send the progress using rabbitmq
    jsonfile.write('[\n')

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            json.dump(row, jsonfile)
            jsonfile.write(',\n')
    jsonfile.write(']')
