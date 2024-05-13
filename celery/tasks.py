
from celery import Celery
from pathlib import Path
import csv
import json

app = Celery (
    'tasks',
    backend='redis://redis:6379',
    broker="amqp://userf:userd@rabbitmq:5672"
    # TODO: these needs to be replaced by env variables 
)

@app.task(name='converter')
def converter(filename: str):

    # this file is full of hacks but the point is to async convert the file 
    # and send the progress to the user
    filename = "./media/" + filename
    jsonFileName = filename.replace('.csv', ".json")

    jsonfile = open(jsonFileName, 'w') 

    print(f'filename = {filename}')
    print(f'jsonfile = {jsonFileName}')
    jsonfile.write('[\n')
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            json.dump(row, jsonfile)
            jsonfile.write(',\n')
    jsonfile.write(']')
    #########################

    return "success"
