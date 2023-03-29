"""gestion_examen URL Configuration

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
from .views import CreateMatiereView, UpdateSalleView, DeleteSalleView,GetSallesView,SalleCreateView


urlpatterns = [
    
    path('salle/create', SalleCreateView.as_view(), name='cours'),
    path('salle/update', UpdateSalleView.as_view(), name='JKJcours'),
    path('salle/delete', DeleteSalleView.as_view(), name='JKours'),
    path('salle/get', GetSallesView.as_view(), name='JKoujjuurs'),
    path('matiere/create', CreateMatiereView.as_view(), name='JKurs'),

    


        ]

