from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage

from .forms import UploadForm as UploadFileForm
from celery import Celery

app = Celery (
    'tasks',
    backend='redis://redis:6379',
    broker="amqp://userf:userd@rabbitmq:5672"
    # TODO: these needs to be replaced by env variables 
)

# app.send_task('readfile', [file])

def home_view(request: HttpRequest):

    if (request.method == 'POST'):
        form = UploadFileForm(request.POST, request.FILES)
        print("______________________________________________________")
        if form.is_valid():
            file = request.FILES.get('file')
            newFile = default_storage.save(file.name, file)
            print(newFile)

        else:
            print("unvalid form")
    else:
        form = UploadFileForm()

    return render(request, "home.html", {"form": form})
