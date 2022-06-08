from django import forms
from django.forms import ModelForm
from .models import Usuario


class RegistroForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['email_usuario','nom_usuario','ape_usuario','contra_usuario', 'rol_usuario']

class LoginForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email_usuario', 'contra_usuario']

class ModUser(ModelForm):
    model = Usuario
    fields = ['nombre_usuario', 'ape_usuario', 'contra_usuario', 'rol_usuario']