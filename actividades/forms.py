from django import forms
from .models import Actividad
from .models import Servicio
from .models import TipoActividad


class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ['Nombre','servicio','Codigo_actividad', 'tipo_actividad', 'Estado_actividad', 'Cupo_Actividad']

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ['Codigo_servicio','nombre']


class TipoActividadForm(forms.ModelForm):

    class Meta:
        model = TipoActividad
        fields = ['Codigo_tipoActividad','nombre']
