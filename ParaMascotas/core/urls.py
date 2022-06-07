from django.urls import path
from .views import home, login, registro, perfil


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
]