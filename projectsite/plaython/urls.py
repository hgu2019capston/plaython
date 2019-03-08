from django.urls import path
from . import views

app_name = 'plaython'
urlpatterns = [
    path('', views.createForm, name='createForm'),
    ]
