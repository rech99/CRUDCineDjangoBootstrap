from django.db import models
from django.contrib.auth.models import User
from generos.models import Genero

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion=models.TextField()
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo 