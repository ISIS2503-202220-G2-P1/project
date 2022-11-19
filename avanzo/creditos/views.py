from django.http import HttpResponse
from .logic import solicitud_logic as sl
from django.core import serializers
import json
import checksum
import uuid
from django.views.decorators.csrf import csrf_exempt
import pickle

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SolicitudCredito
from .serializers import SolicitudCreditoSerializer
import time
from django.contrib.auth.decorators import login_required
from avanzo.auth0backend import getRole


@login_required
@api_view(['GET', 'POST'])
def solicitud_view(request):
    role = getRole(request)
    if role == "Analista":
        if request.method == 'GET':
            id_ = request.GET.get('id', None)
            if id_:
                solicitud_dto = sl.get_solicitud(id_)
                solicitud = SolicitudCreditoSerializer(solicitud_dto, many=False)
                return Response(solicitud.data)

            else:
                solicitudes_dto = sl.get_solicitudes()
                solicitudes = SolicitudCreditoSerializer(
                    solicitudes_dto, many=True)
                return Response(solicitudes.data)
    else:
        return HttpResponse("Unauthorized User")

    if request.method == 'POST':
        # Crea la solicitud
        # Se duerme por 30 segundos simulando el procesamiento
        # Que tendria que hacer Avanzo para determinar si la solicitud
        # es aprobada o no para darle respuesta al usuario
        ser = SolicitudCreditoSerializer(data=request.data)
        if ser.is_valid():
            file_name =  str(uuid.uuid4())
            checksum_calculated = ''
            with open(file_name + '.pkl' ,'w') as f:
                pickle.dump(ser.data,f) 
                checksum_calculated = checksum.get_for_file(file_name + '.pkl')
                f.write(checksum_calculated)

            time.sleep(180)
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)

        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
