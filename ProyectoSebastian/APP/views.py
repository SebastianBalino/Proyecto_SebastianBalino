from django.shortcuts import render, redirect

from .forms import ProductoForm,ContactoForm



# Create your views here.
from django.http import HttpResponse

# Vista de Inicio
def inicio(request):
    return render (request, "APP/index.html")

# Vista de Clientes
def clientes(request):
    return render (request, "APP/clientes.html")

# Vista de Productos
def productos(request):
    return render (request, "APP/productos.html")

# Vista de Contacto
def contacto(request):
    return render (request, "APP/contacto.html")


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto en la base de datos
            return redirect('agregar_producto')  # Cambia el redirect según tu necesidad
    else:
        form = ProductoForm()

    return render(request, 'APP/agregar_producto.html', {'form': form})


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la información del contacto en la base de datos
            return redirect('formcontacto')  # Usa el nuevo nombre del path
    else:
        form = ContactoForm()

    return render(request, 'APP/contacto.html', {'form': form})


