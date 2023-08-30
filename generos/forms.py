from django import forms
from .models import Genero

class CrearGeneroForm(forms.ModelForm):
    class Meta:
        model= Genero
        fields = ['titulo']
        widgets={
            'titulo': forms.TextInput(attrs={'class': 'form-control m-auto', 'placeholder': 'Escribe genero aqui',})
        }

