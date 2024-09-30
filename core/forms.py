from django import forms
from .models import Sprint
from .models import Daily


class SprintUpdateForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['atividades', 'equipe', 'comunicacao', 'entregas']
        widgets = {
            'atividades': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'equipe': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'comunicacao': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'entregas': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
        }

class SprintCreateForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim', 'gerente']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'gerente': forms.Select(attrs={'class': 'form-control'}),
        }

class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['descricao', 'data', 'nota']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
        }