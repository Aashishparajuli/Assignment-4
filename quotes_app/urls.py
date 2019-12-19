
from django.contrib import admin
from django.urls import path
from quotes_app.views import allquotes

urlpatterns = [
    path('all/',allquotes)
]
