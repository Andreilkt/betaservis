from django.contrib import admin

from django.db import models
from beta.models import Betaservis, BetaservisText

#from fly.fly_nsk.models import BetasevisText BetasevisText

@admin.register(Betaservis)
class BetaservisAdmin(admin.ModelAdmin):
    list_display = ("main", "services", "works", "forms", "contacts", "site", "outsorcing", "our_friends")

@admin.register(BetaservisText)
class BetaservisTextAdmin(admin.ModelAdmin):
    list_display = ("main_text", "services_text", "works_text", "forms_text", "contacts_text", "site_text", "outsorcing_text", "our_friends_text")


# Register your models here.
