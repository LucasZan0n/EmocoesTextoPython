# from django.shortcuts import render, redirect
import nltk
nltk.download('punkt')  # Tokenização de textos
from nltk.stem.snowball import SnowballStemmer

from AnaliseSentimentos.models import Letra, Registro
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 
from django.shortcuts import redirect
from LeXmo import LeXmo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Telas de Visualização


class RegistroCreate(CreateView):
    model = Registro
    fields = ['nome',
              'email',
              'senha', ]
    template_name: str = 'registro.html'
    success_url = '/'

# ========================================

class LetraCreate(LoginRequiredMixin, CreateView):
    model = Letra
    fields = ['nomeM', 'letra',]
    template_name: str = 'letra.html'
    login_url: reverse_lazy('login')
    success_url = '/letras/'


    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        instance = form.save(commit=False)


        if self.request.method == "POST":
            letra = self.request.POST['letra']
        
            emo = LeXmo.LeXmo(letra)
            emo.pop('text', None)
            instance.sentimento = emo

            instance.save()
            return url
# ========================================

class LetraList(LoginRequiredMixin,ListView):
    model = Letra
    template_name: str = 'minhasLetras.html'
    queryset = Letra.objects.all().order_by('nomeM')
    login_url: reverse_lazy('login')


    def get_queryset(self):
        self.queryset = Letra.objects.filter(usuario=self.request.user)
        return self.queryset
# ========================================

class lista(LoginRequiredMixin, ListView):
    model = LetraList
    template_name: str = 'lista.html'
    queryset = Letra.objects.order_by('letra')
    sentimento = property('letra')
    login_url: reverse_lazy('login')


    def get_queryset(self):
        self.queryset = Letra.objects.filter(usuario=self.request.user)
        letra_id = self.kwargs['pk']
        return self.queryset
# ========================================

class AtualizarUsuario(LoginRequiredMixin, UpdateView):
    model = Registro
    fields = ['nome',
              'email',
              'senha', ]
    template_name: str = 'editarUsuario.html'
    success_url = '/informacoes/'
    login_url: reverse_lazy('login')


    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

# ========================================

class AtualizarLetra(LoginRequiredMixin, UpdateView):
    model = Letra
    fields = ['nomeM', 'letra',]
    template_name: str = 'editarLetra.html'
    login_url: reverse_lazy('login')
    success_url = '/letras/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        instance = form.save(commit=False)

        if self.request.method == "POST":
            letra = self.request.POST['letra']
        
            emo = LeXmo.LeXmo(letra)
            emo.pop('text', None)
            instance.sentimento = emo

            instance.save()
            return url


# ========================================

class DeletarUsuario(LoginRequiredMixin, DeleteView):
    model = Registro
    template_name = 'deletarUsuario.html'
    success_url = '/'
    login_url: reverse_lazy('login')


    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
# ========================================


class DeletarLetra(LoginRequiredMixin, DeleteView):
    model = Letra
    template_name = 'deletarLetra.html'
    success_url = '/letras/'
    login_url: reverse_lazy('login')
    

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
# ========================================


class ListarUsuario(LoginRequiredMixin, ListView):
    model = Registro
    template_name: str = 'informacoes.html'
    queryset = Registro.objects.all().order_by('nome')
    login_url: reverse_lazy('login')


    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url