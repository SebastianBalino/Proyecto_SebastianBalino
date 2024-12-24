from django.shortcuts import render, redirect

from .forms import ProductoForm,ContactoForm, ClienteForm, ProductoSearchForm

from .models import Producto

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

def sobremi(request):
    return render (request, "APP/sobremi.html")


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


def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clientes')  # Cambia esta URL a donde quieras redirigir después de registrar
    else:
        form = ClienteForm()
    return render(request, 'APP/registrar_cliente.html', {'form': form})


def buscar_producto(request):
    productos = Producto.objects.all()  # Mostrar todos los productos por defecto

    if request.method == 'GET':
        form = ProductoSearchForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            descripcion = form.cleaned_data.get('descripcion')

            # Filtrar productos si se proporcionan parámetros
            if nombre:
                productos = productos.filter(nombre__icontains=nombre)
            if descripcion:
                productos = productos.filter(descripcion__icontains=descripcion)

    else:
        form = ProductoSearchForm()

    return render(request, 'APP/buscar_producto.html', {'form': form, 'productos': productos})