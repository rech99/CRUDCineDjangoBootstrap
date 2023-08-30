from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import CrearGeneroForm
from .models import Genero
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registro usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('generos')
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Usuario ya existe'})

    return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Contraseñas no coinciden.'})

@login_required
def generos(request):
    generos = Genero.objects.filter(user=request.user)
    return render(request, 'generos.html', {'generos': generos})

@login_required
def genero_detalle(request, genero_id):
    if request.method == 'GET':
        genero = get_object_or_404(Genero, pk=genero_id, user = request.user)
        form = CrearGeneroForm(instance=genero)
        return render(request, 'genero_detalles.html', {'genero': genero, 'form': form})
    else:
        try:
            genero = get_object_or_404(Genero, pk=genero_id, user = request.user)
            form = CrearGeneroForm(request.POST, instance=genero)
            form.save()
            return redirect('generos')
        
        except ValueError:
            return render(request, 'genero_detalles.html', {'genero': genero, 'form': form, 'error':'Error al actualizar.'})

@login_required
def eliminar_genero(request, genero_id):
    genero = get_object_or_404(Genero, pk = genero_id, user=request.user)
    if request.method == 'POST':
        genero.delete()
        return redirect ('generos')         

@login_required
def crear_genero(request):
    if request.method == 'GET':
        return render (request, 'crear_genero.html', {'form':CrearGeneroForm})
    
    else:
        try:
            form=CrearGeneroForm(request.POST)
            nuevo_genero=form.save(commit=False)
            nuevo_genero.user= request.user
            nuevo_genero.save()
            return redirect ('generos')
        
        except ValueError:
            return render (request, 'crear_genero.html', {'form':CrearGeneroForm, 'error':'Provee datos validos'})

@login_required
def salir(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error':'Usuario/contraseña invalido(s)' })
        
        else:
            login(request, user)
            return redirect('home')
        
        

