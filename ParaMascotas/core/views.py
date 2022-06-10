from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegistroForm
from .models import Region, Producto, Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#intento de login
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'usuario does not existe')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Contraseña o usuari incorrectos')    
    context = {}
    return render(request, 'core/login.html', context)

##  VISTA ÍNDICE


def home(request):

    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }

    return render(request, 'core/home.html', datos)

##  VISTA LOGIN

#def login(request):
        
    ## usuarios = Usuario.objects.all()

 #   return render(request, 'core/login.html')


##  VISTA REGISTRO

def registro(request):
    
    datos = {
        'form': RegistroForm()
    }

    if request.method=='POST':

        formulario = RegistroForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "El Usuario se ha registrado correctamente.";
        else:
            datos['mensaje'] = "Datos incompletos o inválidos."

    return render(request, 'core/registro.html', datos)

##  VISTA PERFIL

def perfil(request):

    ## usuarios = Usuario.objects.all()

    return render(request, 'core/perfil.html')