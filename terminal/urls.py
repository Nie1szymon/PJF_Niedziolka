from django.urls import path
from django.conf.urls import include
from .views import ListOfTerminal,  change_terminal_stan

urlpatterns = [
    path("", ListOfTerminal, name="listofterminal"),
    path('change_terminal_stan/<int:terminal_id>/', change_terminal_stan, name='change_terminal_stan'),

]