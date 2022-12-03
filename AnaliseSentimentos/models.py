from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# CRUD feito com inputs do próprio Django usando a classe MODEL

def user_path(instance, filename):
    return 'usuario_{0}/{1}'.format(instance.usuario.id, filename)
    
class Registro(models.Model):
    username = models.CharField(max_length=150,)
    password1 = models.CharField(max_length=150,)
    password2 = models.CharField(max_length=150,)


    def __str__(self):
        return "{} ({}) ({})".format(self.username, self.password1, self.password2)

    def get_absolute_url(self):
        return reverse('login')


class Letra(models.Model):
    nomeM = models.CharField(max_length=150, verbose_name='')
    letra = models.TextField(max_length=10000, verbose_name='', unique=True)
    sentimento = models.TextField(max_length=100000)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('minhasLetras')
        
