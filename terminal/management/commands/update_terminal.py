import sys
from django.core.management.base import BaseCommand
from terminal.models import Terminal, Stan

class Command(BaseCommand):
    help = 'Update terminal state based on a file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the file containing terminal states')

    def handle(self, *args, **options):
        file_path = options['file_path']

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    terminal_name = line[:8].strip()
                    new_state = line[8].strip()
                    if new_state == 'Y':
                        new_state_name = 'on_'
                    elif new_state == 'N':
                        new_state_name = 'off'
                    else:
                        self.stdout.write(self.style.WARNING(f'Invalid state "{new_state}" for terminal {terminal_name}'))
                        continue

                    try:
                        terminal = Terminal.objects.get(name=terminal_name)
                        # Pobierz obiekt Stan na podstawie jego name
                        new_state_obj = Stan.objects.get(name=new_state_name)
                        terminal.stan = new_state_obj
                        terminal.save()
                        self.stdout.write(self.style.SUCCESS(f'State of {terminal_name} updated to {new_state_name}'))
                    except Terminal.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'Terminal with name {terminal_name} does not exist'))
                    except Stan.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'State "{new_state_name}" does not exist'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found'))

