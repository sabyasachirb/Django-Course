from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('car/<slug:slug>/', views.CarDetailView.as_view(), name = 'car_detail'),
]
