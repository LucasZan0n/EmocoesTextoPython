from django.contrib.auth.forms import UserCreationForm
from django import forms

from AnaliseSentimentos.models import Registro

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ['nome','email','senha', ]
        