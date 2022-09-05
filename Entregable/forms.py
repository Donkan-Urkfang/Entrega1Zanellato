from django import forms

class DestinosForm(forms.Form):

    pais = forms.CharField()
    ciudad = forms.CharField()

class DatosForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()