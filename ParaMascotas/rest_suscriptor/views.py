from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes #permisos
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework.authentication import TokenAuthentication #autentica token
from rest_framework.permissions import IsAuthenticated #si está autenticado
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_suscrip(request):
    if request.method == 'GET':
        usuario = User.objects.all()
        serializer = UserSerializer(usuario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def gud_user(request, id):
    try:
        usuario = User.objects.get(email=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(usuario)
        return Response(serializer.data)
    if request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(usuario,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


