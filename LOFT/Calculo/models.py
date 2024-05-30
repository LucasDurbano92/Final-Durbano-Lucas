from django.db import models
from decimal import Decimal

def precio_con_impuesto(precio):
    impuesto = Decimal('0.21') * precio
    return precio + impuesto




    # def total_con_impuesto(self):
    #     perimetro = self.calcular_perimetro()
    #     total_varilla = self.varilla.precio_con_impuesto() * perimetro if self.varilla else 0
    #     return total_varilla

