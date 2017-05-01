from django.conf.urls import include, url
from django.contrib import admin
from core import views


urlpatterns = [

    url(r'^$', include('core.urls')),
    url(r'^admin/asistencia/$', views.listado_asistencia, name='listado-asistencia'),
    url(r'^admin/asistencia/(?P<is_refresh>\w+)$', views.listado_asistencia, name='listado-asistencia'),


    url(r'^admin/reporte/(?P<id_estudiante>[\w\-]+)$', views.reporte_asistencia_estudiantes, name='reporte-asistencia'),
    url(r'^admin/reporte/actividad/(?P<id>[\w\-]+)$', views.reporte_estudiantes_inscritos, name='reporte-actividad'),
    url(r'^admin/', admin.site.urls),

    url(r'^estudiante/asistio/(?P<asistencia_id>[\w\-]+)', views.flag_asistio, name='si-asistio'),
    url(r'^estudiante/no-asistio/(?P<asistencia_id>[\w\-]+)', views.flag_no_asistio,
        name='no-asistio'),


    url(r'^estudiante/horas-asistencia/(?P<programacion_id>[\w\-]+)/(?P<asistencia_id>[\w\-]+)', views.agregar_horas_asistencia,
        name='horas-asistencia'),

    # Django-Select2
    url(r'^select2/', include('django_select2.urls')),

    url(r'', include('api.urls')),

]
