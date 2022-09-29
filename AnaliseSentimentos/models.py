from django.db import models

# Create your models here.


class Registro(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    email = models.CharField(max_length=100, verbose_name='Email')
    senha = models.CharField(max_length=150, verbose_name='Senha')

    def __str__(self):
        return "{} ({}) ({})".format(self.nome, self.email, self.senha)

# class Login(models.Model):
#     email = models.CharField(max_length=100)
#     senha = models.CharField(max_length=150)
