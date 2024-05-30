from django.shortcuts import render

from . import models
# Create your views here.
def index(request):
    consulta = models.Venta
    contexto = {"ventas": consulta}
    return render(request, "Varillas/index.html", contexto)