from django import forms
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


##  CLASE REGIONES

class Region(models.Model):
    id_region   = models.IntegerField(primary_key=True, verbose_name='ID Región')
    nom_region  = models.CharField(max_length=40, verbose_name='Nombre Región')

    def __str__(self):
        return self.nom_region


##  CLASE PRODUCTOS
class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name='ID Producto')
    nombre      = models.CharField(max_length=32, verbose_name='Nombre Producto')
    precio      = models.IntegerField()
    region      = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

## CLASE USUARIOS
class Usuario(models.Model):

    class roles(models.TextChoices):
        admin   = 'adm', ('Admin')
        usuario = 'usr', ('Usuario')
        socio   = 'usc', ('Socio')
    email_usuario   = models.EmailField(primary_key=True, max_length=32, verbose_name='Email de Usuario')
    nom_usuario     = models.CharField(max_length=24, verbose_name='Nombre de Usuario')
    ape_usuario     = models.CharField(max_length=24, verbose_name='Apellido de Usuario')
    contra_usuario  = models.CharField(max_length=16, verbose_name='Contraseña de Usuario')
    rol_usuario     = models.CharField(max_length=3, choices=roles.choices, verbose_name='Rol de Usuario')
    ## puntos_usuario  = models.IntegerField(verbose_name='Puntos de Usuario')
    ## mascotas        = models.JSONField()
    ## suscripcion     = models.


    def __str__(self):
        return self.email_usuario


##  CLASE HISTORIAL VENTAS