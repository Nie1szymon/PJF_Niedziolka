from django.urls import path
from django.conf.urls import include
from .views import ListOfTerminal, add_terminal, add_model, terminal_stan_update, ListOfEvent, add_event_exchange, \
    view_event_repair, move_to_history, update_actual_event, import_data_from_file

urlpatterns = [
    path("", ListOfTerminal, name="listofterminal"),
    path("addTerminal/", add_terminal, name='AddTerminal'),
    path("addModel/", add_model, name='AddModel'),
    path("stan_update/<int:pk>/", terminal_stan_update, name="terminal_stan_update"),
    path("add_event_exchange/<int:pk>/", add_event_exchange, name="add_event_exchange"),
    path("ListOfEvent", ListOfEvent, name="listofevent"),
    path("repairEvent", view_event_repair, name="eventsRepair"),
    path('move_to_history/<int:event_id>/', move_to_history, name='move_to_history'),
    path('repair_terminalEvent/<int:pk>/', update_actual_event, name='update_actual_event'),
    path('import_data_from_file/', import_data_from_file, name='import_data'),

]