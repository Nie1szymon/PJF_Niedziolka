from django import forms
from django.http import request
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Stan, ModelTerminal, Terminal, ActualEvent, Action


class AddTerminalForm(forms.ModelForm):
    name = forms.CharField(max_length=16, required=True, label='Nazwa terminala')
    stan = forms.ModelChoiceField(queryset=Stan.objects.all(), required=True, label='Stan terminala')
    model = forms.ModelChoiceField(queryset=ModelTerminal.objects.all(), required=True, label='Model terminala')

    class Meta:
        model = Terminal
        fields = ['name', 'stan', 'model']


class ModelTerminalForm(forms.ModelForm):
    name = forms.CharField(max_length=16, required=True, label='Nazwa terminala')
    year_production = forms.IntegerField(label='Rok Produkcji')

    class Meta:
        model = ModelTerminal
        fields = ['name', 'year_production']


class TerminalStanForm(forms.ModelForm):
    stan = forms.ModelChoiceField(queryset=Stan.objects.all(), required=True, label='Stan terminala')

    class Meta:
        model = Terminal
        fields = ['stan', ]

class EventActionForm(forms.ModelForm):
    dataStart = forms.DateField()
    timeStart = forms.TimeField()
    terminal = forms.ModelChoiceField(queryset=Stan.objects.all(), required=True, label='Stan terminala')
    action = forms.ModelChoiceField(queryset=Stan.objects.all(), required=True, label='Stan terminala')
    description = forms.ModelChoiceField(queryset=Stan.objects.all(), required=True, label='Stan terminala')
    user_id = forms.ModelChoiceField(queryset=Stan.objects.all(), required=True, label='Stan terminala')
    class Meta:
        model = ActualEvent
        fields = ['dataStart','timeStart','action','terminal','description','user_id']
class AddEventFormNaprawa(forms.ModelForm):
    class Meta:
        model = ActualEvent
        fields = ['dataStart', 'terminal', 'description', 'action',]