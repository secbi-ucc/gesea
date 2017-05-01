# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, generics
import django_filters
from rest_framework.response import Response
from inscripcion.models import AsistenciaEstudiante
from .serializers import AsistenciaEstudianteSerializer
from rest_framework import filters
from programacion.models import Programacion
from django.utils.timezone import now

class AsistenciaEstudianteViewSet(viewsets.ModelViewSet):

    serializer_class = AsistenciaEstudianteSerializer
    http_method_names = ('put', 'get')
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('programacion',)
    queryset = AsistenciaEstudiante.objects.all()
    paginate_by = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        serializer_data = serializer.data
        custom_data = {'asistencia_results': {'asistencia_array': serializer_data}}
        return Response(custom_data)




    def get_queryset(self):
        user = self.request.user
        p = Programacion.objects.filter(Instructor__user=1).last()
        return AsistenciaEstudiante.objects.filter(programacion=p, fecha_asistencia=now())