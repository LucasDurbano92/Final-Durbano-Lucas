from django import forms
from django.db import IntegrityError
from Varillas.models import Presupuesto, Cliente

class PresupuestoForm(forms.ModelForm):

    class Meta:
        model = Presupuesto
        fields = ['cliente', 'vendedor', 'vidrio', 'passpartou', 'varilla', 'material', 'color', 'Alto', 'Ancho']

   
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'contacto']
        unique_together = ('nombre', 'apellido', 'contacto')


    def save(self, commit=True):
        try:
            return super().save(commit=commit)
        except IntegrityError:
            self.add_error(None, 'El Cliente ya está registrado.')
            return None