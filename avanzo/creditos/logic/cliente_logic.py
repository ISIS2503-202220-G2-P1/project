from ..models import Cliente

def get_cliente(pk):
    return Cliente.objects.get(pk = pk)