from django.contrib import admin

# Register your models here.
from .models import Producto, Contacto, Cliente

# Registro básico de los modelos en el panel de administración
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(Cliente)