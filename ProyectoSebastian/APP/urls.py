
from django.urls import path
from APP import views

from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes/', views.clientes, name="Clientes"),
    path('productos/', views.productos, name="Productos"),
    path('contacto/', views.contacto, name="Contacto"),
    path('sobremi/', views.sobremi, name="Sobremi"),
    
    
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('contacto/', views.contacto, name='formcontacto'),
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    
    
]

