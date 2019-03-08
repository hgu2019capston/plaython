from django.urls import path
from . import views

app_name = 'playton'
urlpatterns = [
    path('', views.createForm, name='createForm'),
    ]
