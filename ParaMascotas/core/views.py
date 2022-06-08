from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm, ModUser
from .models import Historial, Region, Producto, Usuario


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
            
            return redirect(to='perfil')

            ## AÑADIR UN IF PARA CUANDO EL USUARIO SEA TIPO ADMIN

        else:
            datos['mensaje'] = "Datos incompletos o inválidos."

    return render(request, 'core/registro.html', datos)

##  VISTA PERFIL

def perfil(request):

    ## usuarios = Usuario.objects.all()

    return render(request, 'core/perfil.html')

##  VISTA DE USUARIO ADMINISTRADOR

def administrar(request):

    usuarios    = Usuario.objects.all()
    productos   = Producto.objects.all()
    ventas      = Historial.objects.all()

    return render(request, 'core/administrar.html', usuarios, productos, ventas)

##  FUNCIÓN PARA ELIMINAR USUARIO

def delet_user(resquest, email):

    usuario = Usuario.objects.get(email_usuario = email)

    usuario.delete()

    return redirect(to='administrar')

##  VISTA MODIFICAR USUARIO

def mod_user(request, email):
    
    usuario = Usuario.objects.get(email_usuario = email)

    datos = {
        'form' : ModUser(instance=usuario)
    }



    if request.method=='POST':

        formulario = RegistroForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "El Usuario se ha modificado correctamente.";
            
            return redirect(to='administrar')

