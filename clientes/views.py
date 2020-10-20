from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from .models import Cliente

# Create your views here.
class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'telefono']
    success_url = '/registrar-cliente'