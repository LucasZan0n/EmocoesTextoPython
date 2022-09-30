from django.forms import ModelForm
from AnaliseSentimentos.models import Letra

# Create the form class.
class LetraForm(ModelForm):
    class Meta:
        model = Letra
        fields = ['letra']