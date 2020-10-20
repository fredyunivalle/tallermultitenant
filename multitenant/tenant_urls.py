from django.conf.urls import url
from django.contrib import admin
from clientes.views import ClienteCreateView

urlpatterns = [
    url(r'^registrar-cliente/$', ClienteCreateView.as_view()),
]
