from django import forms
from .models import Actividad
from .models import Servicio


class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ['servicio','Codigo_actividad', 'tipo_actividad', 'Estado_actividad', 'Cupo_Actividad']

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ['Codigo_servicio','nombre']
