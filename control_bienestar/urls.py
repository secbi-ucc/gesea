from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as autenticacion



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'control_bienestar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^actividades/$', 'actividades.views.lista_actividades', name='actividades-lista'),
    url(r'^actividades/detalle/(?P<id_actividad>\d+)', 'actividades.views.detalle_actividad', name='actividades-detalle'),
    url(r'^actividades/nueva/$', 'actividades.views.nueva_actividad', name='actividades-nueva'),
    url(r'^login/$', autenticacion.login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', autenticacion.logout, {'template_name': 'core/logout.html'}, name='logout'),







)
