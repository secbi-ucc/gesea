from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'control_bienestar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^actividades/$', 'actividades.views.lista_actividades', name='actividades-lista'),
    url(r'^actividades/detalle/(?P<id_actividad>\d+)', 'actividades.views.detalle_actividad', name='actividades-detalle'),
    



)
