# export_change.py

from datetime import datetime
from django.core.management.base import BaseCommand


from terminal.models import Terminal, Stan
from django.db.models import Q
from django.db.models import F


class Command(BaseCommand):
    help = 'Export terminals with different next_stan to a text file'

    def handle(self, *args, **options):
        # Pobierz aktualną datę i czas
        now = datetime.now()
        # Utwórz nazwę pliku w formie 'change_data_godzina.txt'
        filename = f'change_{now.strftime("%Y-%m-%d_%H")}.txt'

        # Otwórz plik tekstowy do zapisu
        with open(filename, 'w') as file:

            terminals = Terminal.objects.exclude(Q(stan=F('next_stan')))
            # Iteruj przez każdy terminal i zapisz do pliku
            for terminal in terminals:
                file.write(f'{terminal.name}: {terminal.next_stan}\n')

        # Wyświetl komunikat o sukcesie
        self.stdout.write(self.style.SUCCESS(f'Terminals with different next_stan exported to {filename}'))
