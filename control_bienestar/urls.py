from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as autenticacion



urlpatterns = patterns('',

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
    url(r'^inscripcion/$', 'inscripcion.views.inscripcion_lis', name='lista-inscripcion'),
    url(r'^inscripcion/forms/inscripcionesf/$', 'inscripcion.views.inscripcion_forms', name='forms-inscripcion'),
    url(r'^inscripcion/estudianteslis/$', 'inscripcion.views.estudianteslis', name='lista-estudiantes'),
    url(r'^inscripcion/nuevo/$', 'inscripcion.views.agregar_estudiante', name='estudiante-nuevo'),
    url(r'^estudiante/editar/(?P<id_estudiante>\d+)', 'inscripcion.views.editar_estudiante', name='estudiante-editar'),
    url(r'^estudiante/detalle/(?P<id_estudiante>\d+)', 'inscripcion.views.detalle_estudiante', name='estudiante-detalle'),
    url(r'^inscripcion/forms/usuario/$', 'inscripcion.views.agregar_usuario', name='agregar:usuario'),
    #urls profesor
    url(r'^Profesor/nuevo/$', 'profesor.views.agregar_profesor', name='agregar-profesor'),
    url(r'^profesor/$', 'profesor.views.lista_profesores', name='Lista-profesor'),
    url(r'^Profesor/detalle/(?P<id_ucc>\d+)', 'profesor.views.detalle_profesor', name='profesor-detalle'),
    url(r'^Profesor/editar/(?P<id_ucc>\d+)', 'profesor.views.editar_profesor', name='profesor-editar'),
    #Urls Programacion
    url(r'^horario/$', 'programacion.views.horario_lista', name='horario-lista'),
    url(r'^horario/eliminar/(?P<id_horario>\d+)', 'programacion.views.horario_eliminar', name='horario-eliminar'),
    url(r'^horario/detalle/(?P<id_horario>\d+)', 'programacion.views.horario_detalle', name='horario-detalle'),
    url(r'^dias/$', 'programacion.views.dias_lista', name='dias-lista'),
    url(r'^dias/detalle/(?P<id_dia>\d+)', 'programacion.views.dia_detalle', name='dia-detalle'),
    url(r'^dia/eliminar/(?P<id_dia>\d+)', 'programacion.views.dia_eliminar', name='dia-eliminar'),
    url(r'^dia/editar/(?P<id_dia>\d+)', 'programacion.views.dia_editar', name='dia-editar'),
    url(r'^dia/nuevo$', 'programacion.views.dia_nuevo', name='dia-nuevo'),
    url(r'^programacion/lista$', 'programacion.views.programacion_lista', name='programacion-lista'),
    url(r'^programacion/nueva$', 'programacion.views.programacion_nueva', name='programacion-nueva'),
    url(r'^prgramacion/eliminar/(?P<id_programacion>\d+)', 'programacion.views.programacion_eliminar', name='programacion-eliminar'),
    url(r'^programacion/detalle/(?P<id_programacion>\d+)', 'programacion.views.programacion_detalle', name='programacion-detalle'),
    url(r'^Lugar/$', 'programacion.views.lugares_lista', name='lugar-lista'),
    url(r'^Lugar/detalle/(?P<id_lugar>\d+)', 'programacion.views.lugar_detalle', name='lugar-detalle'),
    url(r'^Lugar/editar/(?P<id_lugar>\d+)', 'programacion.views.lugar_editar', name='lugar-editar'),
    url(r'^Lugar/eliminar/(?P<id_lugar>\d+)', 'programacion.views.lugar_eliminar', name='lugar-eliminar'),
    url(r'^Lugar/nuevo/$', 'programacion.views.lugar_nuevo', name='lugar-nuevo'),



    )
