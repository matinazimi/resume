from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def home(request):

    return render(request,'index.html')

def download_resume(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Expenses01.xlsx"'
    return response
