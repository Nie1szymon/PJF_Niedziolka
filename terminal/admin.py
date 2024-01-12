from django.contrib import admin
from .models import ActualEvent, Action, Terminal, ModelTerminal, Stan, HistoryEvent

# Register your models here.
admin.site.register(ActualEvent)
admin.site.register(HistoryEvent)
admin.site.register(Action)
admin.site.register(Terminal)
admin.site.register(ModelTerminal)
admin.site.register(Stan)
