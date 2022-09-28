from django.db import models

# Create your models here.
class Registro(models.Model):
    nome =  models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=150)