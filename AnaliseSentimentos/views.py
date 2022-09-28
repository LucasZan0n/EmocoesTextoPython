from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse(request, 'index.html')

def form(request):
    return render(request, 'registro.html')