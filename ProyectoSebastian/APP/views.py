from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Vista de Inicio
def inicio(request):
    return HttpResponse("Vista Inicio")

# Vista de Clientes
def clientes(request):
    return HttpResponse("Vista Clientes")

# Vista de Productos
def productos(request):
    return HttpResponse("Vista Productos")

# Vista de Contacto
def contacto(request):
    return HttpResponse("Vista Contacto")