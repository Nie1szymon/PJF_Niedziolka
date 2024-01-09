from django.urls import path
from django.conf.urls import include
from .views import ListOfTerminal,add_terminal, add_model, terminal_stan_update, ListOfEvent

urlpatterns = [
    path("", ListOfTerminal, name="listofterminal"),
    path("addTerminal/", add_terminal, name='AddTerminal'),
    path("addModel/", add_model, name='AddModel'),
    path("stan_update/<int:pk>/", terminal_stan_update, name="terminal_stan_update"),
    path("ListOfEvent", ListOfEvent, name="listofevent"),
]