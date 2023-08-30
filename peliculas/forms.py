from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model= Pelicula
        fields = ['titulo', 'descripcion', 'genero']
        widgets={
            'titulo': forms.TextInput(attrs={'class': 'form-control m-auto', 'placeholder': 'Escribe titulo aqui',}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control m-auto', 'placeholder': 'Escribe descripcion aqui',})
        }



