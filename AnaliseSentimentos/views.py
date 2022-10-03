# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from AnaliseSentimentos.models import Letra, Registro, Login
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.


class LoginCreate(CreateView):
    model = Login
    fields = ['email',
              'senha',
              ]
    template_name: str = 'index.html'
    success_url: reverse_lazy('letra')


class RegistroCreate(CreateView):
    model = Registro
    fields = ['nome',
              'email',
              'senha', ]
    template_name: str = 'registro.html'
    success_url: reverse_lazy('index')


class LetraCreate(CreateView):
    model = Letra
    fields = ['nomeM', 'letra', ]
    template_name: str = 'letra.html'
    success_url: reverse_lazy('minhasLetras')


class LetraList(ListView):
    model = Letra
    template_name: str = 'minhasLetras.html'
    queryset = Letra.objects.all().order_by('nomeM')


class lista(ListView):
    model = LetraList
    template_name: str = 'lista.html'
    queryset = Letra.objects.all().order_by('letra')


# def home(request):
#     data = {}
#     data['db'] = Registro.objects.all()

#     return render(request, 'index.html', data)


# def registro(request):
#     data = {}
#     data['registro'] = RegistroForm()
#     return render(request, 'registro.html', data)


# def novoUsuario(request):
#     form = RegistroForm(request.POST or None)
#     if form.is_valid():
#           form.save()
#           return redirect('home')


# def view(request, pk):
#     data = {}
#     data['db'] = Registro.objects.get(pk=pk)
#     return render(request, 'view.html', data)


# def letra(request):
#     data = {}
#     data['login'] = LoginForm()
#     return render(request, 'letra.html', data)
