from django import forms
from .models import Sprint

class SprintCreateForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['data_inicio', 'data_fim', 'gerente']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }

class SprintUpdateForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['atividades', 'equipe', 'comunicacao', 'entregas']
        widgets = {
            'atividades': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            'equipe': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            'comunicacao': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            'entregas': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }