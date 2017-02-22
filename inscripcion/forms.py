from django import forms
from .models import Estudiantes

class EstudiantesForm(forms.ModelForm):

    class Meta:
        model = Estudiantes
        fields = ['Codigo_estudiante','nombre_1','apellido_1','nid','tipo_nid','programa_academico','genero','semestre','correo','Estado','telefono','ciclo_lectivo']
