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
    #urls de loging & logout
    url(r'^login/$', autenticacion.login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', autenticacion.logout, {'template_name': 'core/logout.html'}, name='logout'),
    #urls de actividades
    url(r'^servicio/$', 'actividades.views.lista_servicios', name='servicios-lista'),
    url(r'^servicio/nuevo/$', 'actividades.views.nuevo_servicio', name='servicio-nuevo'),
    url(r'^servicio/detalle/(?P<id_servicio>\d+)', 'actividades.views.detalle_servicio', name='servicio-detalle'),
    url(r'^servicio/editar/(?P<id_servicio>\d+)', 'actividades.views.editar_servicio', name='servicio-editar'),
    url(r'^servicio/eliminar/(?P<id_servicio>\d+)', 'actividades.views.eliminar_servicio', name='servicio-eliminar'),
    url(r'^actividades/$', 'actividades.views.lista_actividades', name='actividades-lista'),
    url(r'^actividades/nueva/$', 'actividades.views.nueva_actividad', name='actividades-nueva'),
    url(r'^actividades/detalle/(?P<id_actividad>\d+)', 'actividades.views.detalle_actividad', name='actividad-detalle'),
    url(r'^actividades/editar/(?P<id_actividad>\d+)', 'actividades.views.editar_actividad', name='actividad-editar'),
    url(r'^actividades/eliminar/(?P<id_actividad>\d+)', 'actividades.views.eliminar_actividad', name='actividad-eliminar'),
    url(r'^actividades/tipo/$', 'actividades.views.lista_tipoActividades', name='tipoactividades-lista'),
    url(r'^actividades/tipo/nuevo$', 'actividades.views.nuevo_tipoActividad', name='tipoactividades-nuevo'),
    url(r'^actividades/tipo/detalle/(?P<id_tipoactividad>\d+)', 'actividades.views.detalle_tipoActividad', name='tipoactividad-detalle'),
    url(r'^actividades/tipo/editar/(?P<id_tipoactividad>\d+)', 'actividades.views.editar_tipoActividad', name='tipoactividad-editar'),
    url(r'^actividades/tipo/eliminar/(?P<id_tipoactividad>\d+)', 'actividades.views.eliminar_tipoActividad', name='tipoactividad-eliminar'),
    #urls inscripciones
    url(r'^inscripcion/inscripciones/$', 'inscripcion.views.inscripcion_lis', name='lista-inscripcion'),
    url(r'^inscripcion/forms/inscripcionesf/$', 'inscripcion.views.inscripcion_forms', name='forms-inscripcion'),
    url(r'^inscripcion/estudianteslis/$', 'inscripcion.views.estudianteslis', name='lista-estudiantes'),
    url(r'^inscripcion/nuevo/$', 'inscripcion.views.agregar_estudiante', name='estudiante-nuevo'),
    url(r'^estudiantes/editar/(?P<id_Estudiantes>\d+)', 'inscripcion.views.editar_estudiante', name='estudiantes-editar'),
    url(r'^inscripcion/detalle/(?P<id_Estudiantes>\d+)', 'inscripcion.views.detalle_estudiante', name='estudiantes-detalle'),
    url(r'^inscripcion/forms/usuario/$', 'inscripcion.views.agregar_usuario', name='agregar:usuario'),
    #urls profesor
    url(r'^profesor/nuevo/$', 'profesor.views.agregar_profesor', name='agregar-profesor'),
    url(r'^profesor/lista/$', 'profesor.views.lista_profesores', name='Lista-profesor'),
    url(r'^Profesor/detalle/(?P<id_ucc>\d+)', 'profesor.views.detalle_profesor', name='profesor-detalle'),
    url(r'^Profesor/editar/(?P<id_ucc>\d+)', 'profesor.views.editar_profesor', name='profesor-editar'),

    #Urls Programacion
    url(r'^programacion/dia$', 'programacion.views.dia_actividad', name='actividad-dia'),
    url(r'^programacion/horario$', 'programacion.views.horario_actividad', name='actividad-horario'),
    url(r'^programacion/lugar$', 'programacion.views.lugar_actividad', name='actividad-lugar'),
    url(r'^programacion/programacion$', 'programacion.views.programacion_actividad', name='actividades-programada'),
    url(r'^programacion/forms/programacion$', 'programacion.views.programacion_form', name='actividad-programacion'),
    url(r'^programacion/forms/lugar$', 'programacion.views.lugar_form', name='form-lugar'),
    url(r'^programacion/forms/horario$', 'programacion.views.horario_form', name='form-horario'),
    url(r'^programacion/forms/dia$', 'programacion.views.dia_form', name='form-dia'),









    )
