from django.contrib import admin
from django.urls import path, include
from . import views

# from django.conf import settings
# from django.conf.urls.static import static

# /reporting

urlpatterns = [
    path('',  views.index, name="report_index"),
    path('grandprofit/', views.grandprofit, name="grandprofit_report"),
]
