from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("services2/", views.services2, name='services2'),
    path("contact/", views.contact, name='contact'),
    path("signup/", views.signupUser, name='signup'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
]
