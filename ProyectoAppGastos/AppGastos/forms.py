from django import forms

class ObjetivoFormulario(forms.Form):
    Objetivo = forms.CharField()
    MontoDelObjetivo = forms.IntegerField()
    Fecha= forms.CharField()
    Observacion = forms.CharField()


class MovimientosFormulario(forms.Form):
    Fecha= forms.CharField()
    Categoria= forms.CharField()
    Importe= forms.IntegerField()
    Nota= forms.CharField()
    Tipo_movimiento= forms.CharField()


class UsuarioFormulario(forms.Form):
    Nombre= forms.CharField()
    Apellido= forms.CharField()
    Email= forms.EmailField()
    Contraseña = forms.CharField()