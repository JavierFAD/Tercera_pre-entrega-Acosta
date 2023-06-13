from django import forms

class FormularioHerramienta(forms.Form):
    nombre = forms.CharField(max_length=50)
    rastreo = forms.IntegerField()
    calibracion = forms.DateField()
    operario = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=50)
    
class BuscaOperario(forms.Form):
    apellido = forms.CharField()
    
class FormularioLider(forms.Form):
    nombre      = forms.CharField(max_length=50)
    apellido    = forms.CharField(max_length=50)
    legajo      = forms.IntegerField()
    sector      = forms.CharField(max_length=40)

class FormularioOperario(forms.Form):
    nombre      = forms.CharField(max_length=50)
    apellido    = forms.CharField(max_length=50)
    legajo      = forms.IntegerField()
    lider       = forms.CharField(max_length=50)
    funcion     = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)
