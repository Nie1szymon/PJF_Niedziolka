from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Stan(models.Model):
    name = models.CharField(primary_key=True, max_length=16, unique=True)

    def __str__(self):
        return self.name


class ModelTerminal(models.Model):
    name = models.CharField(max_length=16, unique=True)
    year_production = models.IntegerField()

    def __str__(self):
        return self.name


class Terminal(models.Model):
    name = models.CharField(max_length=16, unique=True)
    stan = models.ForeignKey(Stan, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelTerminal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    dataStart = models.DateField()
    timeStart = models.TimeField(null=True)
    dataEnd = models.DateField(null=True)
    timeEnd = models.TimeField(null=True)
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.action}"



