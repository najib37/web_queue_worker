from django.http import FileResponse, HttpRequest
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.views import View
from .forms import UploadForm as UploadFileForm
from django.conf import settings
from celery import Celery
import os
from asgiref.sync import sync_to_async

app = Celery (
    'tasks',
    backend='redis://redis:6379',
    broker="amqp://userf:userd@rabbitmq:5672"
    # TODO: these needs to be replaced by env variables 
)

class HomeView(View):

    async def get(self, request: HttpRequest):
        form = UploadFileForm()
        return render(request, "Home/home.html", {"form": form})

    async def post(self, request: HttpRequest):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get('file')
            filename = await sync_to_async(default_storage.save)(file.name, file)
            await sync_to_async(app.send_task)('converter', [filename])
            return redirect('progress') 
        else:
            print("unvalid form")
        return render(request, "Home/home.html", {"form": form})


class DownloadView(View):
    def get(self, request):
        file_path = os.path.join(settings.MEDIA_ROOT, 'download.json')
        print(file_path)
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='download.json')

class ProgressView(View):
    def get(self, request: HttpRequest):
        return render(request, "Progress/progress.html")
