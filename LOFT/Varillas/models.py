from django.db import models
from decimal import Decimal
from Calculo.models import precio_con_impuesto

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Vendedor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre

        
class Varilla(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def precio_con_impuesto(self):
        return precio_con_impuesto(self.precio)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Vidrio(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def precio_con_impuesto(self):
        return precio_con_impuesto(self.precio)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"    
    
class Passpartou(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def precio_con_impuesto(self):
        return precio_con_impuesto(self.precio)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"    
    
    
    
class Venta(models.Model):
    nombre = models.PositiveIntegerField(unique=True, editable=False, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True, blank=True)
    vidrio = models.ForeignKey(Vidrio, on_delete=models.SET_NULL, null=True, blank=True)
    passpartou = models.ForeignKey(Passpartou, on_delete=models.SET_NULL, null=True, blank=True)
    varilla = models.ForeignKey(Varilla, on_delete=models.SET_NULL, null=True, blank=True)
    Alto = models.DecimalField(max_digits=100, decimal_places=2)
    Ancho = models.DecimalField(max_digits=100, decimal_places=2)
    
    
