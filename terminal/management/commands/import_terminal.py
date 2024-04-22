from django.core.management.base import BaseCommand

from terminal.models import Terminal, Stan, ModelTerminal


class Command(BaseCommand):
    help = 'Import terminal form file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Ścieżka do pliku z danymi terminalem')

    def handle(self, *args, **kwargs):
        # pobieramy ścieżkę do pliku z argumentów
        file_path = kwargs['file_path']

        # otwieramy plik Terminals.txt w trybie odczytu
        with open(file_path, 'r') as file:
            # iterujemy po linijkach w pliku
            for line in file:
                # parsujemy dane z linijki
                name = line[:8].strip()
                stan_name = line[8:11].strip()
                model_name = line[11:].strip()

                # sprawdzamy, czy istnieje stan o podanej nazwie
                try:
                    stan = Stan.objects.get(name=stan_name)
                except Stan.DoesNotExist:
                    print(f'Nie istnieje stan o nazwie "{stan_name}", pomijam terminal "{name}"')
                    continue

                # sprawdzamy, czy istnieje model terminala o podanej nazwie
                try:
                    model = ModelTerminal.objects.get(name=model_name)
                except ModelTerminal.DoesNotExist:
                    print(f'Nie istnieje model terminala o nazwie "{model_name}", pomijam terminal "{name}"')
                    continue
                # sprawdzamy, czy terminal o podanej nazwie już istnieje
                if Terminal.objects.filter(name=name).exists():
                    print(f'Terminal o nazwie "{name}" już istnieje, pomijam dodawanie')
                    continue
                # tworzymy nowy terminal i zapisujemy go w bazie danych
                terminal = Terminal.objects.create(name=name, stan=stan, model=model)
                print(f'Dodano nowy terminal: {terminal}')
