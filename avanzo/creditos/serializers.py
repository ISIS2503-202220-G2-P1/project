from rest_framework import serializers
from . import models

class AnalistaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'cc', 'nombre', 'email')
        model = models.Analista

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'cc', 'nombre', 'email', 'empresa', 'informacion_personal')
        model = models.Cliente


class SolicitudCreditoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'estado', 'cliente', 'analista', 'cantidad', 'plazo_en_meses')
        model = models.SolicitudCredito
