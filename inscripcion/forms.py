from django import forms
from .models import Estudiantes

class EstudiantesForm(forms.ModelForm):

    class Meta:
        model = Estudiantes
        fields = ['Codigo_estudiante','Horas_estudiante','nombre','apellidos','semestre', 'facultad','sexo','Estado','telefono', 'correo']
