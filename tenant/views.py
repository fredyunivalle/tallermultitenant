from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView
from .models import Tenant, Domain
from .utilities import obtener_datos_tenants

# Create your views here.

class TenantCreateView(CreateView):
    model = Tenant
    fields = ['nombre_tenant', 'descripcion']
    success_url = '/registrar-tenant'

    def form_valid(self,form):
        tenant_registrado = form.instance
        tenant_registrado.schema_name = tenant_registrado.nombre_tenant
        self.object = form.save()
        dominio_tenant = Domain(domain=self.object.nombre_tenant+'.localhost',
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()
        return super(TenantCreateView, self).form_valid(form)


class DatosTenantsView(TemplateView):
    template_name = 'tenant/mostrar_datos_tenants.html'

    def get_context_data(self, **kwargs):
        context = super(DatosTenantsView, self).get_context_data(**kwargs)
        context['datos'] = obtener_datos_tenants()
        return context