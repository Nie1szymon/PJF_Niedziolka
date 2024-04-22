from django.contrib import admin
from .models import Terminal, ModelTerminal, Stan, HistoryOfAction

# Register your models here.

admin.site.register(Terminal)
admin.site.register(ModelTerminal)
admin.site.register(Stan)
admin.site.register(HistoryOfAction)
