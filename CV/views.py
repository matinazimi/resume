from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files import File
from resume.settings import BASE_DIR, MEDIA_ROOT
# Create your views here.
def home(request):

    return render(request,'index.html')

def download_resume(request):
    path_to_file = 'mohammad_matin_azimi.pdf'
    f = open(path_to_file, 'rb')
    pdfFile = File(f)
    response = HttpResponse(pdfFile.read())
    response['Content-Disposition'] ='attachment; filename=mohammad_matin_azimi.pdf'
    return response

