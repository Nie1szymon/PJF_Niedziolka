from django import forms
from django.contrib.auth.models import User

from .models import Stan, ModelTerminal, Terminal, HistoryOfAction


class HistoryForm(forms.ModelForm):
    class Meta:
        model = HistoryOfAction
        fields = [ 'new_stan', 'description']