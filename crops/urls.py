

from django.urls import path 
from .views import crop_suggestion , home

urlpatterns = [
    path('',home),
    path('farmhelp/',crop_suggestion)
]