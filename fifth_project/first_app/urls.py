from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.app, name= 'app'),
    path("form/", views.submit_form, name = 'form'),
    path("djangoform/", views.DjangoForm, name = 'djangoform'),
    path("password/", views.PasswordValidation, name = 'password')
]
