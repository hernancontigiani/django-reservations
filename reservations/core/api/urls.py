from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # API Viewsets routers:
    path('', include('core.api.routers')), 
]
