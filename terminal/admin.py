from django.contrib import admin
from .models import Event,Action,Terminal,ModelTerminal,Stan
# Register your models here.
admin.site.register(Event)
admin.site.register(Action)
admin.site.register(Terminal)
admin.site.register(ModelTerminal)
admin.site.register(Stan)