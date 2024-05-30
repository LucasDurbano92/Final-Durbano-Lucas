from django.db import models
from decimal import Decimal

def precio_con_impuesto(precio):
    impuesto = Decimal('0.21') * precio
    return precio + impuesto



def total_con_impuesto(self):
    total_varillas = sum(varilla.precio_con_impuesto() * 5 for varilla in self.varilla.all())
    return total_varillas * 5
        


def __str__(self):
    total = self.total_venta()
    return f"Venta {self.nombre} - Cliente: {self.cliente} - Total: ${total:.2f}"
