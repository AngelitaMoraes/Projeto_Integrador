from django import forms
from .models import Despesa, Receita

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['categoria_despesa', 'valor', 'data']

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['categoria_receita', 'valor', 'data']