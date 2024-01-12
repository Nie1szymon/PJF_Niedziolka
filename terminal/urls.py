from django.urls import path
from django.conf.urls import include
from .views import ListOfTerminal,add_terminal, add_model, terminal_stan_update, ListOfEvent, add_event_exchange

urlpatterns = [
    path("", ListOfTerminal, name="listofterminal"),
    path("addTerminal/", add_terminal, name='AddTerminal'),
    path("addModel/", add_model, name='AddModel'),
    path("stan_update/<int:pk>/", terminal_stan_update, name="terminal_stan_update"),
    path("add_event_exchange/<int:pk>/", add_event_exchange, name="add_event_exchange"),
    path("ListOfEvent", ListOfEvent, name="listofevent"),
    #path("repairEvent", add_event_repair, name="eventsRepair"),

]