from django.shortcuts import render, redirect, get_object_or_404
from .forms import PeliculaForm
from .models import Pelicula
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.db.models import Q

from django.contrib.auth.models import User
# Create your views here.


@login_required
def peliculas(request):
    peliculas = Pelicula.objects.filter(user=request.user)[:4]
    return render(request, 'peliculas.html', {'peliculas': peliculas})

@login_required
def crear_pelicula(request):
    if request.method == 'GET':
        return render (request, 'crear_pelicula.html', {'form':PeliculaForm})
    
    else:
        try:
            form=PeliculaForm(request.POST)
            nuevo_genero=form.save(commit=False)
            nuevo_genero.user= request.user
            nuevo_genero.save()
            return redirect ('peliculas')
        
        except ValueError:
            return render (request, 'crear_genero.html', {'form':PeliculaForm, 'error':'Provee datos validos'})
        
@login_required
def eliminar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk = pelicula_id, user=request.user)
    if request.method == 'POST':
        pelicula.delete()
        return redirect ('peliculas')  
    
@login_required
def pelicula_detalle(request, pelicula_id):
    if request.method == 'GET':
        pelicula = get_object_or_404(Pelicula, pk=pelicula_id, user = request.user)
        form = PeliculaForm(instance=pelicula)
        return render(request, 'pelicula_detalles.html', {'pelicula': pelicula, 'form': form})
    else:
        try:
            pelicula = get_object_or_404(Pelicula, pk=pelicula_id, user = request.user)
            form = PeliculaForm(request.POST, instance=pelicula)
            form.save()
            return redirect('peliculas')
        
        except ValueError:
            return render(request, 'pelicula_detalles.html', {'pelicula': pelicula, 'form': form, 'error':'Error al actualizar.'})
        
