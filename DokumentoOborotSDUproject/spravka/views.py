from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def glavnaya(request):
    return HttpResponse('test')

def neglavnaya(request):
    return render(request, 'index.html')