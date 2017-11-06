from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm


# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            thefile = request.FILES['file']
            return HttpResponse("Hello!")
        else:
            print("Memay")
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def index(request):
    return HttpResponse("Hello!")
