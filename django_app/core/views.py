from django.http import HttpRequest
from django.shortcuts import render

from .forms import UploadForm as UploadFileForm

def home_view(request: HttpRequest):

    if (request.method == 'POST'):
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            # TODO: add the celler worker to process the file
            print("form is valid")

    else:
        form = UploadFileForm()

    return render(request, "home.html", {"form": form})
