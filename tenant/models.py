from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.

class Tenant(TenantMixin):
    nombre_tenant = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)

    auto_create_schema = True

    def __str__(self):
        return self.schema_name

class Domain(DomainMixin):
    pass
