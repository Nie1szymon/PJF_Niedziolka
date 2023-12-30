from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.template import loader

from .forms import TerminaleForm
from .models import Terminale,History

#def history(request):
#    return HttpResponse(History.objects.all())

# Create your views here.
def history(request):
  # Pobierz wszystkie rekordy z tabeli HISTORY
  history = History.objects.all()

  # Połącz tabele HISTORY i TERMINALE
  history = history.select_related('terminal')

  # Wyświetl rekordy
  return render(request, 'historia.html', {
    'history': history,
  })


@login_required
def dodaj_terminal(request):
  if request.method == 'POST':
    form = TerminaleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('lista_terminali')
  else:
    form = TerminaleForm()
  return render(request, 'dodaj_terminal.html', {
    'form': form,
  })


def lista_terminali(request):
  terminal = Terminale.objects.all()
  return render(request, 'lista_terminali.html', {
    'terminal': terminal,
    'csrf_token': get_token()
  })
