from django.db import models
from decimal import Decimal



def precio_con_impuesto(precio):
    impuesto = Decimal('0.21') * precio
    return precio + impuesto


