# Web Queue Worker
## this is a simple Web Queue Worker implementation using django, celery,  rabbitMq, and reddis

the project is a scuffed web interface to upload csv files to a django server, that sends them and to a remote instance of celery that converts them to json and sends them back to the users. 
the point of the project is offload the process intensive of converting the files to a remote web queue, and use rabbitmq to communicate the filename and the progress of processing the files to the server, which in its turn send it to the user using web sockets.

# TECNOLOGIES
- django: web interface / server
- celery: async web queue & task manager
- rabbitmq: communicating between the services
- reddis: stores the result of the celery tasks

# USAGE
docker compose up --build

!! this project is still in DEV
