from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Region, Producto, Usuario


# Create your views here.


##  VISTA ÍNDICE

def home(request):

    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }

    return render(request, 'core/home.html', datos)

##  VISTA LOGIN

def login(request):
        
    ## usuarios = Usuario.objects.all()

    return render(request, 'core/login.html')


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

    return render(request, 'core/registro.html', datos)

##  VISTA PERFIL

def perfil(request):

    ## usuarios = Usuario.objects.all()

    return render(request, 'core/perfil.html')