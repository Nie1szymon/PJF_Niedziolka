from django.forms import ModelForm
from .models import Terminale,History

class TerminaleForm(ModelForm):
    class Meta:
        model = Terminale
        fields = ['nazwa', 'opis']

class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ["data","time","terminal"]