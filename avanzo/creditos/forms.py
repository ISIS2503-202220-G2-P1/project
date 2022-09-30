from django import forms
from .models import Cliente, Analista, SolicitudCredito


class SolicitudCreditoForm(forms.ModelForm):
    class Meta:
        model = SolicitudCredito
        fields = [
            'estado',
            'cliente',
            'analista',
            'cantidad',
            'plazo_en_meses'
        ]
        labels = {
            'estado' : 'Estado',
            'cliente': 'Cliente',
            'analista': 'Analista',
            'cantidad': 'Cantidad',
            'plazo_en_meses': 'Plazo'
        }
