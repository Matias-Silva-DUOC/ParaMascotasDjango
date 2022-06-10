from django.urls import path
from .views import home, registro, perfil #login
from .import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),

    path('', home, name="home"),
    #path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
]