from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from Varillas.models import Presupuesto, Venta
from Calculo.forms import PresupuestoForm, ClienteForm

def index(request):
    return render(request, 'Calculo/index.html')

def cliente_nuevo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                cliente = form.save()
                if cliente:
                    return redirect('Calculo:crear_presupuesto')
            except IntegrityError:
                form.add_error(None, 'El Cliente ya está registrado.')
    else:
        form = ClienteForm()
    
    return render(request, 'Calculo/cliente_nuevo.html', {'form': form})

def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'Calculo/lista_presupuestos.html', {'presupuestos': presupuestos})

def crear_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Calculo:lista_presupuestos')
    else:
        form = PresupuestoForm()
    return render(request, 'Calculo/crear_presupuesto.html', {'form': form})

def ver_presupuesto(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    return render(request, 'Calculo/ver_presupuesto.html', {'presupuesto': presupuesto})

def borrar_presupuesto(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    presupuesto.delete()
    return redirect('Calculo:lista_presupuestos')

def borrar_todos_presupuestos(request):
    Presupuesto.objects.all().delete()
    return redirect('Calculo:lista_presupuestos')

def enviar_a_venta(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    venta = Venta(
        cliente=presupuesto.cliente,
        vendedor=presupuesto.vendedor,
        vidrio=presupuesto.vidrio,
        passpartou=presupuesto.passpartou,
        varilla=presupuesto.varilla,
        material=presupuesto.material,
        color=presupuesto.color,
        Alto=presupuesto.Alto,
        Ancho=presupuesto.Ancho,
    )

    venta.save()
    presupuesto.delete() 
    return redirect('Calculo:lista_presupuestos')

def enviar_todos_a_venta(request):
    presupuestos = Presupuesto.objects.all()
    for presupuesto in presupuestos:
        venta = Venta(
            cliente=presupuesto.cliente,
            vendedor=presupuesto.vendedor,
            vidrio=presupuesto.vidrio,
            passpartou=presupuesto.passpartou,
            varilla=presupuesto.varilla,
            material=presupuesto.material,
            color=presupuesto.color,
            Alto=presupuesto.Alto,
            Ancho=presupuesto.Ancho,
        )
        venta.save()
        presupuesto.delete()
    return redirect('Varillas:index')

