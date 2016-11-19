from django import forms
from .models import Programacion
from .models import Lugar
from .models import DiaActividad
from bootstrap4_datetime.widgets import DateTimePicker

class ProgramacionForm(forms.ModelForm):
    Fecha_Inicio = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False}))
    Fecha_Final = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False}))

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
