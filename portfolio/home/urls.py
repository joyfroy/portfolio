from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("home", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path("Privacy", views.Privacy, name='Privacy'),
    path("terms", views.terms, name='terms'),
    path("login", views.login, name='login'),

]