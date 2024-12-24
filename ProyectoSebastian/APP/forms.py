from django import forms

from .models import Producto,Contacto,Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad'] 
        
        


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email']
        
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion']
        
class ProductoSearchForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, label='Nombre del Producto')
    descripcion = forms.CharField(max_length=100, required=False, label='Descripción del Producto')