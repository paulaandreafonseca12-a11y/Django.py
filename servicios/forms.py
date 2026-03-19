from django import forms # type: ignore
from django.forms import ModelForm # type: ignore
from django.contrib.admin.widgets import FilteredSelectMultiple # type: ignore
from .models import Servicios


class serviciosForm(ModelForm):
    class Meta:
        model = Servicios
        fields=['nombre', 'precio', 'duracion', ]
        
class serviciosEditarForm(ModelForm):
    class Meta:
        model = Servicios
        fields = '__all__'
        