from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('form/', views.form, name="Infoform"),
    path('form2/', views.form2, name="Infoform2"),
    path('formfreshers/', views.formfreshers, name="Infoformfreshers"),
    path('contact/', views.contact, name="contact"),
    path('finalresume/', views.finalresume, name="finalresume"),
    path('trial/', views.trial, name="trial"),
    path('freshers/', views.freshers, name="freshers"),
    path('about/', views.about, name="about"),
]



