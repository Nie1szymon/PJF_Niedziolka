from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import AddTerminalForm, ModelTerminalForm, TerminalStanForm, ActualEventForm, \
    ActualEventUpdateForm, ImportFileForm
from .models import Terminal, ActualEvent, Action, HistoryEvent, ModelTerminal, Stan


def user_belongs_to_Operatorzy(user):
    return user.is_authenticated and (user.groups.filter(name='OPERATORZY').exists() or user.is_staff)


@login_required
def terminal_stan_update(request, pk):
    terminal = Terminal.objects.get(pk=pk)
    form = TerminalStanForm(instance=terminal)

    if request.method == 'POST':
        form = TerminalStanForm(request.POST, instance=terminal)
        if form.is_valid():
            form.save()
            event = HistoryEvent(
                dataStart=timezone.now(),
                timeStart=timezone.now(),
                dataEnd=timezone.now(),
                timeEnd=timezone.now(),
                terminal=terminal,
                description=f"Zmieniono stan na '{terminal.stan}'",
                action=Action.objects.get(pk=1),
                user_id=request.user,
            )
            event.save()

            return redirect('listofterminal')

    return render(request, 'terminal/edit_terminal_stan.html', {'form': form})


@login_required
def add_terminal(request):
    if request.method == 'POST':
        form = AddTerminalForm(request.POST)
        if form.is_valid():
            terminal = form.save()

            event = HistoryEvent(
                dataStart=timezone.now(),
                dataEnd=timezone.now(),
                terminal=terminal,
                description=f"Dodano terminal",
                action=Action.objects.get(pk=3),
                user_id=request.user,
            )
            event.save()
            return redirect('listofterminal')
    else:
        form = AddTerminalForm()
    return render(request, 'terminal/new_terminal.html', {'form': form})


@login_required
def add_event_exchange(request, pk):
    terminal = get_object_or_404(Terminal, pk=pk)
    form_terminal_stan = TerminalStanForm(instance=terminal)
    form_actual_event = ActualEventForm()

    if request.method == 'POST':
        form_terminal_stan = TerminalStanForm(request.POST, instance=terminal)
        form_actual_event = ActualEventForm(request.POST)

        if form_terminal_stan.is_valid() and form_actual_event.is_valid():
            form_terminal_stan.save()
            description = form_actual_event.cleaned_data['description']

            if description:
                event = ActualEvent(
                    dataStart=timezone.now(),
                    timeStart=timezone.now(),
                    dataEnd=None,
                    timeEnd=None,
                    terminal=terminal,
                    description=f"zgłoszono terminal do naprawy z powodu: {description}",
                    action=Action.objects.get(pk=4),
                    user_reporting=request.user,
                )
                event.save()

            return redirect('listofterminal')

    return render(request, 'terminal/exchange_terminal_stan.html', {
        'form_terminal_stan': form_terminal_stan,
        'form_actual_event': form_actual_event,
    })


@login_required
def add_model(request):
    if request.method == 'POST':
        form = ModelTerminalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listofterminal')
    else:
        form = AddTerminalForm()
    return render(request, 'terminal/new_model.html', {'form': form})


# Create your views here.
@login_required
def ListOfTerminal(request):
    terminals = Terminal.objects.all()
    terminals = terminals.select_related('stan')
    terminals = terminals.select_related('model')

    return render(request, "terminal/list_of_terminal.html", {'terminals': terminals})


@user_passes_test(user_belongs_to_Operatorzy)
def ListOfEvent(request):
    events_h = HistoryEvent.objects.all()
    events_h = events_h.select_related('terminal')
    events_h = events_h.select_related('action')
    events_h = events_h.select_related('user_id')
    events_h = events_h.order_by('-dataEnd')

    events_a = ActualEvent.objects.all()
    events_a = events_a.select_related('terminal')
    events_a = events_a.select_related('action')
    events_a = events_a.select_related('user_reporting')
    events_a = events_a.order_by('dataStart')

    return render(request, "terminal/list_of_events.html", {'eventsH': events_h, 'eventsA': events_a})


@user_passes_test(user_belongs_to_Operatorzy)
def view_event_repair(request):
    events_a = ActualEvent.objects.all()
    events_a = events_a.select_related('terminal')
    events_a = events_a.select_related('action')
    events_a = events_a.select_related('user_reporting')
    events_a = events_a.order_by('dataStart')

    events_a_completed = events_a.filter(~Q(dataEnd=None))
    events_a_pending = events_a.filter(dataEnd__isnull=True)
    print(events_a_completed)
    print(events_a_pending)
    context = {
        'eventsA_completed': events_a_completed,
        'eventsA_pending': events_a_pending,
    }

    return render(request, "terminal/repairEvent.html", context)


@user_passes_test(user_belongs_to_Operatorzy)
def move_to_history(request, event_id):
    actual_event = ActualEvent.objects.get(pk=event_id)

    if request.method == 'POST':
        # Tworzenie obiektu w tabeli HistoryEvent na podstawie obiektu w tabeli ActualEvent
        history_event = HistoryEvent.objects.create(
            dataStart=actual_event.dataStart,
            timeStart=actual_event.timeStart,
            dataEnd=timezone.now(),
            timeEnd=timezone.now(),
            terminal=actual_event.terminal,
            action=actual_event.action,
            description=f"{actual_event.description} - Problem został rozwiązany przez {request.user}",
            user_id=actual_event.user_reporting,
        )

        # Usunięcie obiektu z tabeli ActualEvent
        actual_event.delete()

        return redirect('eventsRepair')

    return render(request, 'terminal/repairEvent.html')


@user_passes_test(user_belongs_to_Operatorzy)
def update_actual_event(request, pk):
    actual_event = get_object_or_404(ActualEvent, pk=pk)

    if request.method == 'POST':
        form = ActualEventUpdateForm(request.POST, instance=actual_event)
        if form.is_valid():
            form.save()
            return redirect('eventsRepair')
    else:
        form = ActualEventUpdateForm(instance=actual_event)

    return render(request, 'terminal/repair_terminal.html', {'form': form, 'actual_event': actual_event})


def import_data_from_file(request):
    file_path = "C:\\Users\\Szymo\\Desktop\\terminal.txt"  # Stała ścieżka do pliku tekstowego

    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line)
                # Przetwarzanie linii i zapis do bazy danych
                name = line[:8].strip()  # Pierwsze 8 znaków to name
                stan_code = line[8:11].strip()  # Następne 3 znaki to stan
                model_name = line[-16:].strip()  # Ostatnie 16 znaków to model

                # Pobieranie obiektów Stan i ModelTerminal na podstawie kodu i nazwy
                stan = Stan.objects.get(name=stan_code)
                model = ModelTerminal.objects.get(name=model_name)

                # Tworzenie nowego obiektu Terminal i zapis do bazy danych
                terminal = Terminal.objects.create(name=name, stan=stan, model=model)
                terminal.save()

        message = "Dane zaimportowane poprawnie."
    except Exception as e:
        message = f"Błąd podczas importowania danych: {str(e)}"

    return render(request, 'terminal/list_of_terminal.html', {'message': message})