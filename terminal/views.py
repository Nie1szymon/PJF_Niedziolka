from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import HistoryForm
from .models import Terminal, ModelTerminal, Stan, HistoryOfAction


def user_belongs_to_Operatorzy(user):
    return user.is_authenticated and (user.groups.filter(name='OPERATORZY').exists() or user.is_staff)


# Create your views here.
@login_required
def ListOfTerminal(request):
    terminals = Terminal.objects.all()
    terminals = terminals.select_related('stan')
    terminals = terminals.select_related('model')
    terminals = terminals.select_related('next_stan')

    return render(request, 'terminal/list_of_terminal.html', {'terminals': terminals})


def change_terminal_stan(request, terminal_id):
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            terminal_change = form.save(commit=False)
            terminal_change.terminal_id = terminal_id
            terminal_change.date_zgloszenia = timezone.now()
            terminal_change.time_zgloszenia = timezone.now()
            terminal_change.user = request.user
            terminal_change.save()
            # Aktualizuj next_stan w modelu Terminal
            terminal = Terminal.objects.get(pk=terminal_id)
            terminal.next_stan = terminal_change.new_stan
            terminal.save()
            return redirect('listofterminal')  # Przekieruj na stronę powodzenia
    else:
        form = HistoryForm()
    return render(request, 'terminal/change_terminal_stan.html', {'form': form})


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
