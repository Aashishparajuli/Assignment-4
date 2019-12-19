
from django.contrib import admin
from django.urls import path
from friend_app.views import allfriends

urlpatterns = [
    path('all/', allfriends)
]
