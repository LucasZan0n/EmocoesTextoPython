# from django.shortcuts import render, redirect
import nltk
nltk.download('punkt')  # Tokenização de textos
from nltk.stem.snowball import SnowballStemmer

from AnaliseSentimentos.models import Letra, Registro, Login
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView 
from django.shortcuts import redirect, render
from LeXmo import LeXmo

# Create your views here.

class LoginCreate(CreateView):
    model = Login
    fields = ['email',
              'senha',
              ]
    template_name: str = 'index.html'


class RegistroCreate(CreateView):
    model = Registro
    fields = ['nome',
              'email',
              'senha', ]
    template_name: str = 'registro.html'


class LetraCreate(CreateView):
    model = Letra
    fields = ['nomeM', 'letra',]
    template_name: str = 'letra.html'

    def form_valid(self, form):
        instance = form.save(commit=False)

        if self.request.method == "POST":
            letra = self.request.POST['letra']
        
            emo = LeXmo.LeXmo(letra)
            emo.pop('text', None)
            instance.sentimento = emo

            instance.save()
            return redirect('/letras/')

    


class LetraList(ListView):
    model = Letra
    template_name: str = 'minhasLetras.html'
    queryset = Letra.objects.all().order_by('nomeM')


class lista(ListView):
    model = LetraList
    template_name: str = 'lista.html'
    queryset = Letra.objects.order_by('letra')
    sentimento = property('letra')

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
