from asyncio.windows_events import NULL
from logging import PlaceHolder
from django.db import models

# Create your models here.


class Registro(models.Model):
    nome = models.CharField(max_length=150,)
    email = models.CharField(max_length=100, verbose_name='Email')
    senha = models.CharField(max_length=150, verbose_name='Senha')

    def __str__(self):
        return "{} ({}) ({})".format(self.nome, self.email, self.senha)


class Login(models.Model):
    email = models.CharField(max_length=100, verbose_name='Email')
    senha = models.CharField(max_length=150)
    ativa = models.BooleanField(default=True)

    registro = models.ForeignKey(Registro, on_delete=models.PROTECT)

    def __str__(self):
        return " ({})".format(self.registro.nome)


class Letra(models.Model):
    nomeM = models.CharField(max_length=150, verbose_name='',  blank=True)
    letra = models.TextField(max_length=100000, verbose_name='')
    # sentimento = models.Exists()

    login = models.ForeignKey(Login, on_delete=models.PROTECT)

    def __str__(self):
        return " ({})".format(self.login)
