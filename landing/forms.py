from django import forms
from .models import Inscricao
from .models import Depoimento


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['email']


class DepoimentoForm(forms.ModelForm):
    class Meta:
        model = Depoimento
        fields = ['nome', 'mensagem']
