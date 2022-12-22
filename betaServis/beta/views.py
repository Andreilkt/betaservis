from django.shortcuts import render

import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Betaservis, BetaservisText

# получение данных из бд
def index(request):
    beta = Betaservis.objects.all()
    return render(request, "index.html", {"beta": beta} )

# Create your views here.
