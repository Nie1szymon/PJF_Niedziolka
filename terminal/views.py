from django.shortcuts import render
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Terminal, Event, Stan, ModelTerminal, Action
from .forms import AddTerminalForm, ModelTerminalForm, TerminalStanForm
from django.contrib.auth.decorators import login_required


@login_required
def terminal_stan_update(request, pk):
    terminal = Terminal.objects.get(pk=pk)
    form = TerminalStanForm(instance=terminal)

    if request.method == 'POST':
        form = TerminalStanForm(request.POST, instance=terminal)
        if form.is_valid():
            form.save()
            event = Event(
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

            event = Event(
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
    events = Event.objects.all()
    events = events.select_related('terminal')
    events = events.select_related('action')
    events = events.select_related('user_id')

    return render(request, "terminal/list_of_events.html", {'events': events})
