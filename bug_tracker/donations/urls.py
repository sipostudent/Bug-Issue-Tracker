from django.urls import path
from . import views

urlpatterns = [
    path('donations', views.Donations.as_view(), name='donations'),
    path('charge', views.charge, name='charge')
]
