from django.conf.urls import url, include
from rest_framework import routers
from .views import AsistenciaEstudianteViewSet, LoginViewCustom, LogoutViewViewCustom

router = routers.DefaultRouter()
router.register(r'asistencia', AsistenciaEstudianteViewSet)


urlpatterns = [
    url(r'^rest-auth/login/$', LoginViewCustom.as_view(), name='rest_login'),
    url(r'^rest-auth/logout/$', LogoutViewViewCustom.as_view(), name='rest_logout'),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),
]