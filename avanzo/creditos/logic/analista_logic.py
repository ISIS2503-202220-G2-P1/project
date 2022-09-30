from ..models import Analista 

def get_analista(pk):
    return Analista.objects.get(pk = pk)