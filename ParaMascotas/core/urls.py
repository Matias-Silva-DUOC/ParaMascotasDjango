from django.urls import path
from .views import delet_user, home, login, registro, perfil


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('delet-user/<email>', delet_user, name=delet_user),    ##  TENER FE
]