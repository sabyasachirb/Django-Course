from django.urls import path
from . import views

urlpatterns = [
    path("buy/<int:pk>/", views.BuyCarView.as_view(), name="buy_car"),
]
