from django.core.checks import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.timezone import now
from django.http import JsonResponse

from .models import Terminal, ActualEvent, Stan, ModelTerminal, Action , HistoryEvent
from .forms import AddTerminalForm, ModelTerminalForm, TerminalStanForm, AddEventFormNaprawa
from django.contrib.auth.decorators import login_required


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
def add_event_exchange(request,pk):
    terminal = Terminal.objects.get(pk=pk)
    form = TerminalStanForm(instance=terminal)

    if request.method == 'POST':
        form = TerminalStanForm(request.POST, instance=terminal)
        if form.is_valid():
            form.save()
            event = ActualEvent(
                dataStart=timezone.now(),
                timeStart=timezone.now(),
                dataEnd=None,
                timeEnd=None,
                terminal=terminal,
                description=f"zgłoszono terminal do wymiany",
                action=Action.objects.get(pk=1),
                user_id=request.user,
            )
            event.save()

            return redirect('listofterminal')

    return render(request, 'terminal/exchange_terminal_stan.html', {'form': form})


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


@login_required
def ListOfEvent(request):
    events_h = HistoryEvent.objects.all()
    events_h = events_h.select_related('terminal')
    events_h = events_h.select_related('action')
    events_h = events_h.select_related('user_id')

    events_a = ActualEvent.objects.all()
    events_a = events_a.select_related('terminal')
    events_a = events_a.select_related('action')
    events_a = events_a.select_related('user_id')

    return render(request, "terminal/list_of_events.html", {'eventsH': events_h, 'eventsA': events_a})
