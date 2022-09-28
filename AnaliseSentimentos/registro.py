from django.forms import ModelForm
from AnaliseSentimentos.models import Registro

# Create the form class.
class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = ['nome', 'email', 'senha']