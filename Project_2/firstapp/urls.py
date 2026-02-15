from django.urls import path, include
from . import views
urlpatterns = [
    path('about/<int:id>', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('', views.index, name = 'home')
]
