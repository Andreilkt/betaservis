"""betaServis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from beta import views

urlpatterns = [
    path("", views.index),
    path("indexx", views.indexx),
    path('main/', views.main, name='main'),
    path('services/', views.services, name='services'),
    path('works/', views.works, name='works'),
    path('forms/', views.forms, name='forms'),
    path('contacts/', views.contacts, name='contacts'),
    path('site/', views.site, name='site'),
    path('our_friends/', views.our_friends, name='our_friends'),

    path('admin/', admin.site.urls),



]

