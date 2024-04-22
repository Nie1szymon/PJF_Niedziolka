from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Stan(models.Model):
    name = models.CharField(primary_key=True, max_length=3, unique=True)

    def __str__(self):
        return self.name


class ModelTerminal(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Terminal(models.Model):
    name = models.CharField(max_length=16, unique=True)
    stan = models.ForeignKey(Stan, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelTerminal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TerminalToChange(models.Model):
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    new_stan = models.ForeignKey(Stan, on_delete=models.CASCADE)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.terminal}"
