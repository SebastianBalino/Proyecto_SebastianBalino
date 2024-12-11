from django.db import models



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Nuevo campo de precio

    def __str__(self):
        return self.nombre
    
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre