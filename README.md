# Web Queue Worker
## this is a simple Web Queue Worker implementation using django, celery,  rabbitMq,  and reddis

the project is a scuffed web interface to csv upload  files to a django server, that takes those files and sends them to an instance of celery that converts them to json and sends them to the users. 
the point of the project is offload the process incentive process of converting the files to its service, and use rabbitmq to communicate the name of the file and the progress of processing the files to the server, which in its turn send it to the user.

# TECNOLOGIES
- django: web interface / server
- celery: async task manager
- rabbitmq: communicating between the services
- reddis: stores the result of the celery tasks
