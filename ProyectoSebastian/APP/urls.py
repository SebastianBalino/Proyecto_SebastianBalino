
from django.urls import path
from APP import views

from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('sobremi/', views.sobremi, name="Sobremi"),
    
    path('clientes/', views.clientes, name="Clientes"),
    path('productos/', views.productos, name="Productos"),
    path('contacto/', views.contacto, name="Contacto"),
    
    
    
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('contacto/', views.contacto, name='formcontacto'),
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    
    path('producto/<int:producto_id>/editar/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'), 
    
    path('productos_lista/', views.productos_lista, name='productos_lista'),
    
    
]

