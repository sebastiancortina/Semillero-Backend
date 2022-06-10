from django.contrib import admin
from django.urls import path, include

from apps.semilleros.views import SemillerolistAV, SemilleroDetalleAV, SemillerolistAprobado
from apps.usuarios.views import UsuariolistAV,  UsuarioDetalleAV

urlpatterns = [
    path('list', SemillerolistAV.as_view(), name='semillero-list'),
    path('<int:id>', SemilleroDetalleAV.as_view(), name='semillero-detalle'),
    path('aprobados', SemillerolistAprobado.as_view(), name='semillero-aprobado'),

    path('usuarios/list',  UsuariolistAV.as_view(), name=' usuario-list'),
    path('usuarios/<int:id>',  UsuarioDetalleAV.as_view(), name=' usuario-detalle')
]
