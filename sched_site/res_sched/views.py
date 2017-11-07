import uuid

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
            savefile = str(uuid.uuid4()) + ".dat"
            print(savefile)
            with open(savefile, "wb+") as f:
                for chunk in thefile.chunks():
                    f.write(chunk)
            resdict = solveit.delay(savefile)
            vardict = resdict.get()
            return HttpResponse("<html><body><p>" + str(vardict) +
                                "</p></body></html>")
        else:
            print("Bad file!")
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def index(request):
    return HttpResponse("Hello!")
