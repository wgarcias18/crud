from django import forms
from .models import Pais


class ProveForm(forms.ModelForm):
    paises = forms.ModelChoiceField(queryset=Pais.objects.filter(status=1),
                                            required=True,
                                            widget=forms.Select(attrs={'col': '6', 'class': 'select2'}))
    nombre = forms.CharField(label=u"Nombre", required=True,
                    widget=forms.Textarea(
                        attrs={'col': '12', 'rows': '3', 'placeholder': 'noombre'}))
    estado = forms.TextField(label=u"Estado", required=True,
                    widget=forms.Textarea(
                        attrs={'col': '12', 'rows': '3', 'placeholder': 'estado'}))
    marca = forms.TextField(label=u"Marca", required=True,
                    widget=forms.Textarea(
                        attrs={'col': '12', 'rows': '3', 'placeholder': 'marca'}))

