from django.contrib import admin
from django.urls import path

from .views import contactView, successView


app_name = 'mail'

urlpatterns = [
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
]