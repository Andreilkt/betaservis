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

def indexx(request):
    betas = Betaservis.objects.all()
    #betatext = BetaservisText.object.all()
    return render(request, "index.html", {"betas": betas })


def main (request):

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        #BetaservisText = BetaservisText()
        BetaservisText.main_text  = request.POST.get("main_text")

    # передаем данные в шаблон
    main_text  = BetaservisText.objects.all()
    return render(request, "main.html", {"main_text": main_text })
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
        BetaservisText.works_text  = request.POST.get("works_text")

    # передаем данные в шаблон
    works_text  = BetaservisText.objects.all()
    return render(request, "works.html", {"works_text": works_text })

def forms  (request):

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        #BetaservisText = BetaservisText()
        BetaservisText.forms_text  = request.POST.get("forms_text")

    # передаем данные в шаблон
    forms_text  = BetaservisText.objects.all()
    return render(request, "forms.html", {"forms_text": forms_text })
