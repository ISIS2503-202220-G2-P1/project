from ..models import SolicitudCredito
from .cliente_logic import get_cliente
from .analista_logic import get_analista

def get_solicitudes():
    return SolicitudCredito.objects.all().first()

def get_solicitud(solicitud_pk):
    return SolicitudCredito.objects.get(pk=solicitud_pk)

def create_solicitud(solicitud):
    estado = solicitud['estado']
    cliente = solicitud['cliente'] 
    analista = solicitud['analista'] 
    cantidad = solicitud['cantidad'] 
    plazo_en_meses = solicitud['plazo_en_meses']

    cliente_dto = get_cliente(cliente)
    analista_dto = get_analista(analista)
    nueva_solicitud = SolicitudCredito(estado=estado, cliente=cliente_dto, analista=analista_dto, cantidad=cantidad, plazo_en_meses=plazo_en_meses)
    nueva_solicitud.save()

    return nueva_solicitud