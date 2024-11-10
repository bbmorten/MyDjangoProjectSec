from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static
from .views import register, profile

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]

