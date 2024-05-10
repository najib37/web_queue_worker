FROM python:3.11

WORKDIR /home/

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
