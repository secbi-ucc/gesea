# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from inscripcion.models import AsistenciaEstudiante
from .serializers import AsistenciaEstudianteSerializer, UserSerializer, ProgramacionSerializer, DiaActividadSerializer
from rest_framework import filters
from programacion.models import Programacion, DiaActividad
from django.utils.timezone import now
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from rest_framework.response import Response
from inscripcion.models import Inscripcion, Estudiantes
from core.views import get_day_hours
from rest_framework.request import Request


class LoginViewCustom(LoginView):
    authentication_classes = (TokenAuthentication,)

class LogoutViewViewCustom(LogoutView):
    authentication_classes = (TokenAuthentication,)


class UserViewSet(APIView):

    """
        View to get current user

        * Requires token authentication.
    
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        return corrent logged user
        """
        user_request = request.user

        user = User.objects.get(id=user_request.id)


        serializer = UserSerializer(user)

        print serializer

        return Response(serializer.data)

class ProgramacionViewSet(viewsets.ModelViewSet):

    serializer_class = ProgramacionSerializer
    http_method_names = ('get',)
    filter_backends = (filters.DjangoFilterBackend,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Programacion.objects.all()
    filter_fields = ('Dia_semana__Dia_Actividad',)
    paginate_by = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        serializer_data = serializer.data
        custom_data = {'pogramacion_results': {'pogramacion_array': serializer_data}}
        return Response(custom_data)


    def get_queryset(self):
        user = self.request.user
        return Programacion.objects.filter(Instructor__user=user)





class AsistenciaEstudianteViewSet(viewsets.ModelViewSet):
    """
    
   `get`:
    Retorna una instacia de asistencia
    
    `list`:
    Retorna una lista de asistencia
    
    `update`:
    Actualiza el numero de horas de una asistencia
    
    """

    serializer_class = AsistenciaEstudianteSerializer
    http_method_names = ('put', 'get')
    filter_backends = (filters.DjangoFilterBackend,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
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
        p = Programacion.objects.filter(Instructor__user=user).last()
        return AsistenciaEstudiante.objects.filter(programacion=p)


class listado_asistencia(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = AsistenciaEstudianteSerializer
    queryset = AsistenciaEstudiante.objects.all()



    def get(self, request, programacion_id):

        serializer_context = {
            'request': Request(request),
        }

        p = Programacion.objects.get(id=programacion_id)

        a = AsistenciaEstudiante.objects.filter(programacion=p, fecha_asistencia=now()).filter()

        serializer = AsistenciaEstudianteSerializer(a, many=True, context=serializer_context)

        custom_data = {'asistencia_results': {'asistencia_array': serializer.data}}

        return Response(custom_data)

    def post(self, request, programacion_id):

        user = request.user
        #pr = Instructor.objects.get(user = user)
        a = None
        p = Programacion.objects.get(id=programacion_id)
        h = get_day_hours(p)
        i = Inscripcion.objects.filter(programacion=p)




        e = Estudiantes.objects.filter(ID_Estudiante__in=list(Inscripcion.objects.filter(programacion=p).values_list('estudiante', flat=True)))

        a = AsistenciaEstudiante.objects.filter(programacion=p, fecha_asistencia=now()).filter()

        if not a:

            for i in range(len(e)):
                AsistenciaEstudiante(programacion=p, estudiante=e[i]).save()

            a = AsistenciaEstudiante.objects.filter(programacion = p, fecha_asistencia=now())
            if a:

                r = {'status': 'created'}
                return Response(r)

        else:

            r = {'status': 'retrived'}
            return Response(r)