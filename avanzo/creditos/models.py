from django.db import models

class Cliente(models.Model):
    cc = models.TextField()
    nombre = models.TextField()
    email = models.TextField()
    empresa = models.TextField()
    informacion_personal = models.TextField()

    def __str__(self):
        return f'Cliente con CC {self.cc} y nombre {self.nombre}'

class Analista(models.Model):
    cc = models.TextField()
    nombre = models.TextField()
    email = models.TextField()

    def __str__(self):
        return f'Analista con CC {self.cc} y nombre {self.nombre}'


class SolicitudCredito(models.Model):
    estado = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    analista = models.ForeignKey(Analista,on_delete = models.CASCADE)
    cantidad = models.DecimalField(decimal_places = 4, max_digits = 10)
    plazo_en_meses = models.IntegerField()

    def __str__(self):
        return f'Solicitud de credito del Cliente {self.cliente}'