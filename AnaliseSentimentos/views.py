# from django.shortcuts import render, redirect
import nltk
from LeXmo import LeXmo

nltk.download('punkt')  # Tokenização de textos
from nltk.stem.snowball import SnowballStemmer

from AnaliseSentimentos.models import Letra, Registro

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


# Telas de Visualização

class RegistroCreate(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registro.html'
    success_url = reverse_lazy('login')


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
        return self.queryset


    def get_object(self, queryset = None):
        self.object = get_object_or_404 (Letra, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

# ========================================

# class AtualizarUsuario(LoginRequiredMixin, UpdateView):
#     model = Registro
#     fields = ['username',
#               'password1',
#               'password2' ]
#     template_name: str = 'editarUsuario.html'
#     success_url = '/informacoes/'
#     login_url: reverse_lazy('login')


#     def form_valid(self, form):
#         form.instance.usuario = self.request.user
#         url = super().form_valid(form)
#         return url


#     def get_object(self, queryset = None):
#         self.object = get_object_or_404 (Registro, pk=self.kwargs['pk'])
#         return self.object

    
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


    def get_object(self, queryset = None):
        self.object = get_object_or_404 (Letra, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


# ========================================

# def DeletarUsuario(request, id):
#     registro = get_object_or_404(Registro, pk=id)
#     registro.delete()
#     return redirect('login')


# ========================================


class DeletarLetra(LoginRequiredMixin, DeleteView):
    model = Letra
    template_name = 'deletarLetra.html'
    success_url = '/letras/'
    login_url: reverse_lazy('login')
    

    def get_object(self, queryset = None):
        self.object = get_object_or_404 (Letra, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
# ========================================


# class ListarUsuario(LoginRequiredMixin, ListView):
#     model = Registro
#     template_name: str = 'informacoes.html'
#     queryset = Registro.objects.all().order_by('username')
#     login_url: reverse_lazy('login')

