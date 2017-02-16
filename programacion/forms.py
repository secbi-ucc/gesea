from django import forms
from .models import Programacion
from .models import Lugar
from .models import DiaActividad


class ProgramacionForm(forms.ModelForm):

    class Meta:
        model = Programacion
        fields = ['Servicio','actividad', 'TipodeParticipacion', 'lugarActividad','Dia_semana','profesor', 'Fecha_Inicio','Fecha_Final']

class LugarForm(forms.ModelForm):

    class Meta:
        model = Lugar
        fields = ['NombreLugar']

class DiaForm(forms.ModelForm):

    class Meta:
        model = DiaActividad
        fields = ['Dia_Actividad','Horario']
