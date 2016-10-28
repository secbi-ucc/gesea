from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as autenticacion



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'control_bienestar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'core.views.inicio', name='inicio'),
    url(r'^no-permitido/', 'core.views.no_permitido', name='no-permitido'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^actividades/$', 'actividades.views.lista_actividades', name='actividades-lista'),
    url(r'^actividades/detalle/(?P<id_actividad>\d+)', 'actividades.views.detalle_actividad', name='actividades-detalle'),
    url(r'^actividades/nueva/$', 'actividades.views.nueva_actividad', name='actividades-nueva'),
    url(r'^login/$', autenticacion.login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', autenticacion.logout, {'template_name': 'core/logout.html'}, name='logout'),

url(r'^actividades/servicios1/$', 'actividades.views.agregar_servicios', name='agregar-servicios'),

url(r'^actividades/forms/servicioslis/$', 'actividades.views.lista_servicio', name='lista-servicios'),

url(r'^inscripcion/inscripciones/$', 'inscripcion.views.inscripcion_lis', name='lista-inscripcion'),

url(r'^inscripcion/forms/inscripcionesf/$', 'inscripcion.views.inscripcion_forms', name='forms-inscripcion'),

url(r'^inscripcion/estudianteslis/$', 'inscripcion.views.estudianteslis', name='lista_estudiantes'),

url(r'^inscripcion/forms/usuario/$', 'inscripcion.views.agregar_usuario', name='agregar:usuario'),

url(r'^profesor/profesoragr/$', 'profesor.views.agregar_prof', name='agregar_profesor'),

url(r'^profesor/forms/profesorf/$', 'profesor.views.profesor_forms', name='forms_profesor'),

url(r'^actividades/agregar$', 'actividades.views.agregar_actividad', name='actividades-agregada'),

url(r'^actividades/forms/servicio$', 'actividades.views.servicio_actividad', name='actividad-servicio'),

url(r'^actividades/forms/tipo$', 'actividades.views.tipo_actividad', name='actividad-tipo'),

url(r'^programacion/dia$', 'programacion.views.dia_actividad', name='actividad-dia'),

url(r'^programacion/horario$', 'programacion.views.horario_actividad', name='actividad-horario'),

url(r'^programacion/lugar$', 'programacion.views.lugar_actividad', name='actividad-lugar'),

url(r'^programacion/programacion$', 'programacion.views.programacion_actividad', name='actividades-programada'),

url(r'^programacion/forms/programacion$', 'programacion.views.programacion_form', name='actividad-programacion'),

url(r'^programacion/forms/lugar$', 'programacion.views.lugar_form', name='form-lugar'),

url(r'^programacion/forms/horario$', 'programacion.views.horario_form', name='form-horario'),

url(r'^programacion/forms/dia$', 'programacion.views.dia_form', name='form-dia'),









)
