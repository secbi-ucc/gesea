from django.conf.urls import include, url
from django.contrib import admin
from core import views


urlpatterns = [

    url(r'^$', include('core.urls')),
    url(r'^admin/asistencia/$', views.listado_asistencia, name='listado-asistencia'),
    url(r'^admin/asistencia/(?P<is_refresh>\w+)$', views.listado_asistencia, name='listado-asistencia'),
    url(r'^admin/', admin.site.urls),

    url(r'^estudiante/asistio/(?P<asistencia_id>[\w\-]+)', views.flag_asistio, name='si-asistio'),
    url(r'^estudiante/no-asistio/(?P<asistencia_id>[\w\-]+)', views.flag_no_asistio,
        name='no-asistio'),

    # Django-Select2
    url(r'^select2/', include('django_select2.urls')),

]
