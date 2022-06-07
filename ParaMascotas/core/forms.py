from django import forms
from django.forms import ModelForm
from .models import Usuario


class RegistroForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['id_usuario','nom_usuario','ape_usuario','email_usuario','contra_usuario', 'rol_usuario']