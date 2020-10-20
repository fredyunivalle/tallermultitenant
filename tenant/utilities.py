from .models import Tenant
from clientes.models import Cliente
from django.db import connection

def obtener_datos_tenants():
    """
    Función para retornar el nombre y los datos de clientes de cada tenant
    :return:
    """

    datos = []
    tenants = Tenant.objects.exclude(schema_name='public')
    for tenant in tenants:
        connection.set_tenant(tenant)
        datos_tenant_actual = {
            'nombre_tenant': tenant.nombre_tenant,
            'clientes_tenant': list(Cliente.objects.all())
        }
        datos.append(datos_tenant_actual)
    connection.set_schema_to_public()
    return datos
