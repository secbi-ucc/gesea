from django.conf.urls import url, include
from rest_framework import routers
from .views import AsistenciaEstudianteViewSet


router = routers.DefaultRouter()
router.register(r'asistencia', AsistenciaEstudianteViewSet)


urlpatterns = [
    url(r'^api/auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),
]