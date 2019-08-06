from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<id>/', views.details, name='details'),
    path('details/<id>/edit/', views.edit_details, name='edit_details'),
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('details/<id>/delete/', views.delete_ticket, name='delete_ticket')
]
