from django.contrib import admin

from .models import Cliente, Analista, SolicitudCredito

admin.site.register(Cliente)
admin.site.register(Analista)
admin.site.register(SolicitudCredito)