# Web Queue Worker

## Overview
This is a simple Web Queue Worker implementation using Django, Celery, RabbitMQ, and Redis.

The project provides a web interface to upload CSV files to a Django server. The server sends the files to a remote instance of Celery, which converts them to JSON and sends them back to the users. The main goal of the project is to offload the process-intensive task of converting the files to a remote web queue. RabbitMQ is used to communicate the filename and the progress of processing the files to the server, which then sends the information to the user using web sockets.

## Notes
- The design and UI won't be a big focus of the project; they are only to show the other functionality.
- This project is intended to explore Django ASGI model async request-response cycle deeply.
- Get familiar with RabbitMQ and the microservices architecture.
- Use Remote Celery Instance.

## Features
- Upload CSV files via a web interface
- Asynchronous processing of CSV files to JSON
- Real-time progress updates using web sockets
- Offload processing tasks to a remote queue

## Technologies
- **Django**: Web interface / server
- **Celery**: Asynchronous web queue & task manager
- **RabbitMQ**: Communication between services
- **Redis**: Stores the result of the Celery tasks

## Usage
To start the project, use the following command:
```sh
docker compose up --build
```
### To generate a large csv use the scripe in the shared_date directory

## Site
The web interface can be accessed at:
```
http://localhost:7070
```

## Links
- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryproject.org/en/stable/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [Redis](https://redis.io/)

## Screenshots
![screen 1](https://github.com/user-attachments/assets/18382c0c-0b23-448b-81af-c348437690d5)
![screen 2](https://github.com/user-attachments/assets/f94ca41f-5a7b-4b74-a84e-43484b8348fe)
![screen 3](https://github.com/user-attachments/assets/a31c3f18-191b-4ea1-8ad6-258efda9bd05)
