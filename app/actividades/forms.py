from django import forms
from .models import Actividad
from .models import Area


class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ['servicio','Codigo_actividad', 'tipo_actividad', 'Estado_actividad', 'Cupo_Actividad']

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = ['Codigo_servicio','nombre']
