from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),

    path('', home, name="home"),
    #path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    #ev 4
    path('tienda/', tienda, name='tienda'),
    path('carrito/', carrito, name='carrito'),
    path('checkout/', checkout, name='checkout'),
    
]