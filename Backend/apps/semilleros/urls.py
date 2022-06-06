from django.contrib import admin
from django.urls import path, include
from apps.semilleros.views import SemillerolistAV, SemilleroDetalleAV


urlpatterns = [
    path('list/', SemillerolistAV.as_view(), name='semillero-list'),
    path('semillero/<int:id>', SemilleroDetalleAV.as_view(), name='semillero-detalle')
]
