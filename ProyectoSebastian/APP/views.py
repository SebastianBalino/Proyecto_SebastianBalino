from django.shortcuts import render, redirect , get_object_or_404

from .forms import ProductoForm,ContactoForm, ClienteForm, ProductoSearchForm

from .models import Producto


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpResponse

# Vista de Inicio
def inicio(request):
    return render (request, "APP/index.html")

def sobremi(request):
    return render (request, "APP/sobremi.html")

# Vista de clientes
@login_required
def clientes(request):
    return render (request, "APP/clientes.html")

# Vista de Productos
@login_required
def productos(request):
    return render (request, "APP/productos.html")

# Vista de Contacto
@login_required
def contacto(request):
    return render (request, "APP/contacto.html")




@login_required
def agregar_producto(request):
    if not request.user.is_superuser:
        return redirect('Productos')  # Redirige a otra página si no es superusuario
    
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto en la base de datos
            return redirect('Productos')  # Redirige a la lista de productos o donde prefieras
    else:
        form = ProductoForm()

    return render(request, 'APP/agregar_producto.html', {'form': form})

@login_required
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la información del contacto en la base de datos
            return redirect('formcontacto')  # Usa el nuevo nombre del path
    else:
        form = ContactoForm()

    return render(request, 'APP/contacto.html', {'form': form})

@login_required
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clientes')  
    else:
        form = ClienteForm()
    return render(request, 'APP/registrar_cliente.html', {'form': form})

@login_required
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


@login_required
def actualizar_producto(request, producto_id):
    if not request.user.is_superuser:
        return redirect('Productos')  # Redirige a otra página si no es superusuario
    
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Productos')  # Redirige a la lista de productos o donde prefieras
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'APP/producto_form.html', {'form': form})

@login_required
def eliminar_producto(request, producto_id):
    if not request.user.is_superuser:
        return redirect('Productos')  # Redirige a otra página si no es superusuario
    
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()  # Elimina el producto de la base de datos
        return redirect('Productos')  # Redirige a la lista de productos después de eliminar
    
    return render(request, 'APP/eliminar_producto.html', {'producto': producto})

@login_required
def productos_lista(request):
    productos = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'APP/productos_lista.html', {'productos': productos})