# from django.shortcuts import render, redirect
import nltk
nltk.download('punkt')  # Tokenização de textos
from nltk.stem.snowball import SnowballStemmer

from AnaliseSentimentos.models import Letra, Registro
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 
from django.shortcuts import redirect
from LeXmo import LeXmo

# Telas de Visualização


class RegistroCreate(CreateView):
    model = Registro
    fields = ['nome',
              'email',
              'senha', ]
    template_name: str = 'registro.html'


# ========================================

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

    
# ========================================

class LetraList(ListView):
    model = Letra
    template_name: str = 'minhasLetras.html'
    queryset = Letra.objects.all().order_by('nomeM')

def lista_detail(request, id):
    lista = lista.objects.filter(id = id)
    return redirect("lista.html", context ={"lista":lista})

# ========================================

class lista(ListView):
    model = LetraList
    template_name: str = 'lista.html'
    queryset = Letra.objects.order_by('letra')
    sentimento = property('letra')
    

# ========================================

class AtualizarUsuario(UpdateView):
    model = Registro
    fields = ['nome',
              'email',
              'senha', ]
    template_name: str = 'editarUsuario.html'
    success_url = '/informacoes/'


# ========================================

class AtualizarLetra(UpdateView):
    model = Letra
    fields = ['nomeM', 'letra',]
    template_name: str = 'editarLetra.html'

    def form_valid(self, form):
        instance = form.save(commit=False)

        if self.request.method == "POST":
            letra = self.request.POST['letra']
        
            emo = LeXmo.LeXmo(letra)
            emo.pop('text', None)
            instance.sentimento = emo

            instance.save()
            return redirect('/letras/')


# ========================================

class DeletarUsuario(DeleteView):
    model = Registro
    template_name = 'deletarUsuario.html'
    success_url = '/'


# ========================================



class DeletarLetra(DeleteView):
    model = Letra
    template_name = 'deletarLetra.html'
    success_url = '/letras/'

    
# ========================================


class ListarUsuario(ListView):
    model = Registro
    template_name: str = 'informacoes.html'
    queryset = Registro.objects.all().order_by('nome')