from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .tasks import solveit


# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            thefile = request.FILES['file']
            with open("tempo.dat", "wb+") as f:
                for chunk in thefile.chunks():
                    f.write(chunk)
            solveit.delay("tempo.dat")
            return HttpResponse("beep")
        else:
            print("Memay")
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def index(request):
    return HttpResponse("Hello!")
