from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # autres URLs existantes
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('export/excel/', views.export_excel, name='export_excel'),
    # ...
]