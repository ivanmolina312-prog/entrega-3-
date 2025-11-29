from django import forms
from .models import Auto



class CrearAuto(forms.Form):
    marca = forms.CharField( max_length= 30)
    modelo = forms.CharField( max_length= 30)
    imagen = forms.ImageField(required=False)

class BuscarAuto(forms.Form):
    modelo = forms.CharField(max_length=30, required=False)

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ["marca", "modelo", "year", "kilometros"]