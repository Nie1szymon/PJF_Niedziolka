from django.db import models

class Terminale(models.Model):
    nazwa = models.CharField(max_length=16)
    opis = models.TextField(blank=True)
    def __str__(self):
        return self.nazwa
class History(models.Model):
    data = models.DateField()
    time = models.TimeField()
    terminal = models.ForeignKey(Terminale,on_delete=models.CASCADE,null=True)
    stan = models.CharField(max_length=8)
    def __str__(self):
        return f"{self.data} {self.time} {self.terminal} {self.stan} "
