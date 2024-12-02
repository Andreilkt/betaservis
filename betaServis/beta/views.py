from django.shortcuts import render

import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Betaservis, BetaservisText


# получение данных из бд
def index(request):
    beta = Betaservis.objects.all()
    # betatext = BetaservisText.object.all()
    return render(request, "menu.html", {"beta": beta})


def indexx(request):
    betas = Betaservis.objects.all()
    # betatext = BetaservisText.object.all()
    return render(request, "index.html", {"betas": betas})


def main(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        # BetaservisText = BetaservisText()
        BetaservisText.main_text = request.POST.get("main_text")

    # передаем данные в шаблон
    main_text = BetaservisText.objects.all()
    return render(request, "main.html", {"main_text": main_text})


def services(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        # BetaservisText = BetaservisText()
        BetaservisText.services_text = request.POST.get("services_text")

    # передаем данные в шаблон
    services_text = BetaservisText.objects.all()
    return render(request, "services.html", {"services_text": services_text})


def works(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        # BetaservisText = BetaservisText()
        BetaservisText.works_text = request.POST.get("works_text")

    # передаем данные в шаблон
    works_text = BetaservisText.objects.all()
    return render(request, "works.html", {"works_text": works_text})


def forms(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        # BetaservisText = BetaservisText()
        BetaservisText.forms_text = request.POST.get("forms_text")

    # передаем данные в шаблон
    forms_text = BetaservisText.objects.all()
    return render(request, "forms.html", {"forms_text": forms_text})


def contacts(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        # BetaservisText = BetaservisText()
        BetaservisText.contacts_text = request.POST.get("contacts_text")

    # передаем данные в шаблон
    contacts_text = BetaservisText.objects.all()
    return render(request, "contacts.html", {"contacts_text": contacts_text})


def site(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        # BetaservisText = BetaservisText()
        BetaservisText.site_text = request.POST.get("site_text")

    # передаем данные в шаблон
    site_text = BetaservisText.objects.all()
    return render(request, "site.html", {"site_text": site_text})



def our_friends(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        # BetaservisText = BetaservisText()
        BetaservisText.our_friends_text = request.POST.get("our_friends_text")

    # передаем данные в шаблон
    our_friends_text = BetaservisText.objects.all()
    return render(request, "site.html", {"our_friends_text": our_friends_text})


