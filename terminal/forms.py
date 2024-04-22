from django import forms
from django.contrib.auth.models import User

from .models import Stan, ModelTerminal, Terminal, TerminalToChange


class TerminalChangeForm(forms.ModelForm):
    class Meta:
        model = TerminalToChange
        fields = ['new_stan', 'description']
        widgets = {
            'new_stan': forms.Select(),
        }

    def __init__(self, terminal, *args, **kwargs):
        super(TerminalChangeForm, self).__init__(*args, **kwargs)
        self.fields['new_stan'].queryset = terminal.model.stan_set.all()  # Ustawienie queryset na stany tego modelu
        self.fields['model'] = forms.CharField(initial=terminal.model.name, disabled=True)
        self.fields['stan'] = forms.CharField(initial=terminal.stan.name, disabled=True)
        self.terminal = terminal

    def save(self, commit=True):
        instance = super(TerminalChangeForm, self).save(commit=False)
        instance.terminal = self.terminal
        if commit:
            instance.save()
        return instance