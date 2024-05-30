from django.db import models
from django import forms
from Varillas.models import Vendedor, Cliente, Varilla, Venta

class NuevoVendedor(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre']

class NuevoCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'contacto']

class NuevaVarilla(forms.ModelForm):
    class Meta:
        model = Varilla
        fields = ['nombre', 'precio']

class Ventas(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['Nro_Venta', 'cliente', 'vendedor', 'producto']