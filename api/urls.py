from django.conf.urls import url, include
from .routers import DefaultRouterWithSimpleViews
from .views import (AsistenciaEstudianteViewSet, LoginViewCustom, LogoutViewViewCustom,
                    UserViewSet, ProgramacionViewSet, listado_asistencia)

router = DefaultRouterWithSimpleViews()
router.register(r'asistencia/estudiante', AsistenciaEstudianteViewSet)
router.register(r'programacion', ProgramacionViewSet)
router.register(r'user', UserViewSet, 'user')
router.register(r'login', LoginViewCustom, 'login')
router.register(r'logout', LogoutViewViewCustom, 'logout')



urlpatterns = [
    #url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/asistencia/lista/(?P<programacion_id>\d+)/$', listado_asistencia.as_view()),
    url(r'^api/auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),
]