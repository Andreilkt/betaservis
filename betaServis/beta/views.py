from django.shortcuts import render

import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Betaservis, BetaservisText

# получение данных из бд
def index(request):
    beta = Betaservis.objects.all()
    #betatext = BetaservisText.object.all()
    return render(request, "menu.html", {"beta": beta })

def text(requests):
    beta_text = BetaservisText.object.all()
    return render(requests, "index.html", {"beta_text": beta_text })
# Create your views here.
