"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from AnaliseSentimentos.views import AtualizarLetra, AtualizarUsuario, DeletarLetra, LoginCreate, RegistroCreate, LetraCreate, LetraList, lista

# Definindo as rotas dentro da classe URLS

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', LoginCreate.as_view(), name='index'),
    path('registro/', RegistroCreate.as_view(), name='registro'),

    path('letra/', LetraCreate.as_view(), name='letra'),
    path('letras/', LetraList.as_view(), name='minhasLetras'),
    path('lista/', lista.as_view(), name='lista'),

    path('editar/registro/<int:pk>', AtualizarUsuario.as_view(), name='editarUsuario'),
    path('editar/letra/<int:pk>', AtualizarLetra.as_view(), name='letra'),

    path('excluir/letra/<int:pk>', DeletarLetra.as_view(), name='letra'),


]
