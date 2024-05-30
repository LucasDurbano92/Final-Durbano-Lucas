from django.contrib import admin
from . import models

admin.site.register(models.Cliente)
admin.site.register(models.Vendedor)
admin.site.register(models.Varilla)
admin.site.register(models.Vidrio)
admin.site.register(models.Passpartou)
admin.site.register(models.Venta)

