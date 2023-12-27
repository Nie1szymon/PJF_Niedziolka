from django.shortcuts import render
from django.http import HttpResponse
from .models import Terminale,History

def history(request):
    return HttpResponse(History.objects.all())

# Create your views here.
