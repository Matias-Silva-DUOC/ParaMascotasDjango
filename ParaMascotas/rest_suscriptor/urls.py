from django.urls import path
from rest_suscriptor.views import lista_suscrip, gud_user
from rest_suscriptor.viewsLogin import login


urlpatterns = [
    path('lista_suscrip',lista_suscrip,name="lista_suscriptores"),
    path('gud_user/<id>',gud_user,name="gud_usuarios"),
    path('login',login,name="login")
]