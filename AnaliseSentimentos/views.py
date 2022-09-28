from django.shortcuts import render
from AnaliseSentimentos.registro import RegistroForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def registro(request):
    data = {}
    data['registro'] = RegistroForm()
    return render(request, 'registro.html', data)