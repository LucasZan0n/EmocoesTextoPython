from django.shortcuts import render, redirect
from AnaliseSentimentos.models import Registro
from AnaliseSentimentos.registro import RegistroForm

# Create your views here.


def home(request):
    data = {}
    data['db'] = Registro.objects.all()

    return render(request, 'index.html', data)


def registro(request):
    data = {}
    data['registro'] = RegistroForm()
    return render(request, 'registro.html', data)


def novoUsuario(request):
    form = RegistroForm(request.POST or None)
    if form.is_valid():
          form.save()
          return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Registro.objects.get(pk=pk)
    return render(request, 'view.html', data)
 

# def letra(request):
#     data = {}
#     data['login'] = LoginForm()
#     return render(request, 'letra.html', data)