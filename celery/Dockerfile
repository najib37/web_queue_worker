FROM python:3.11

WORKDIR /home/

COPY requirements.txt ./
RUN pip install -r requirements.txt
# COPY . .

CMD celery -A tasks worker --loglevel=info
# CMD ["celery" "-A" "tasks" "worker" "--loglevel=INFO"]
