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


def services(request):

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        #BetaservisText = BetaservisText()
        BetaservisText.services_text = request.POST.get("services_text")

    # передаем данные в шаблон
    betaservist = BetaservisText.objects.all()
    return render(request, "services.html", {"betaservist": betaservist})

def works  (request):

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        #BetaservisText = BetaservisText()
        Betaservis.works  = request.POST.get("works")

    # передаем данные в шаблон
    works  = Betaservis.objects.all()
    return render(request, "works.html", {"works": works })
