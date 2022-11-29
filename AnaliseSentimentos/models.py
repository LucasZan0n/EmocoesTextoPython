from django.urls import reverse
from django.db import models


# CRUD feito com inputs do próprio Django usando a classe MODEL

class Registro(models.Model):
    nome = models.CharField(max_length=150,)
    email = models.CharField(max_length=100, verbose_name='Email')
    senha = models.CharField(max_length=150, verbose_name='Senha')

    def __str__(self):
        return "{} ({}) ({})".format(self.nome, self.email, self.senha, )

    def get_absolute_url(self):
        return reverse('login')


class Letra(models.Model):
    nomeM = models.CharField(max_length=150, verbose_name='')
    letra = models.TextField(max_length=10000, verbose_name='', unique=True)
    sentimento = models.TextField(max_length=100000, verbose_name='', unique=True)
 
    def get_absolute_url(self):
        return reverse('minhasLetras')
        
