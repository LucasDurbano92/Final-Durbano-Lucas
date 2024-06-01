from django.shortcuts import render
from Varillas.models import Venta, Cliente


def index(request):
    ventas = Venta.objects.all()
    contexto = {"ventas": ventas}
    return render(request, "Varillas/index.html", contexto)

def lista_ventas(request):
    query = request.GET.get('q')
    ventas = Venta.objects.all()
    if query:
        ventas = ventas.filter(venta__nombre__icontains=query) | ventas.filter(venta__apellido__icontains=query)
    
    return render(request, 'varillas/lista_ventas.html', {'ventas': ventas, 'query': query})