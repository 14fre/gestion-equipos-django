from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_equipos, name='lista_equipos'),
    path('registrar/', views.registrar_equipo, name='registrar_equipo'),
    path('editar/<int:equipo_id>/', views.editar_equipo, name='editar_equipo'),
    path('eliminar/<int:equipo_id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('reportar/', views.reportar_danio, name='reportar_danio'),
    path('equipo/<int:equipo_id>/', views.detalle_equipo, name='detalle_equipo'),
]