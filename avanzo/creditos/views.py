from django.http import HttpResponse
from .logic import solicitud_logic as sl
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
import time

@csrf_exempt
def solicitud_view(request):
    if request.method == 'GET':
        id_ = request.GET.get('id', None)
        if id_:
            solicitud_dto = sl.get_solicitud(id_)
            solicitud = serializers.serialize('json', [solicitud_dto,])
            return HttpResponse(solicitud, 'application/json')

        else:
            solicitudes_dto = sl.get_solicitudes()
            solicitudes = serializers.serialize('json', [solicitudes_dto])
            return HttpResponse(solicitudes, 'application/json')

    if request.method == 'POST':
        # Crea la solicitud
        solicitud_dto = sl.create_solicitud(json.loads(request.body))
        # Se duerme por 30 segundos simulando el procesamiento
        # Que tendria que hacer Avanzo para determinar si la solicitud
        # es aprobada o no para darle respuesta al usuario
        time.sleep(30)
        solicitud = serializers.serialize('json', [solicitud_dto ,])
        return HttpResponse(solicitud, 'application/json')