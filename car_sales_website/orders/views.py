from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from cars.models import Car
# Create your views here.
class BuyCarView(LoginRequiredMixin, View):
    def post(self, request, pk):
        car = Car.objects.get(pk=pk)
        quantity = int(request.POST.get('quantity', 1))
        if quantity > car.quantity:
            return render(request, 'car_detail.html', {
                'car': car,
                'error': 'Not enough cars in stock.'
            })
        Order.objects.create(user=request.user, car=car, quantity=quantity)
        car.quantity -= quantity
        car.save()
        return redirect('car_detail', pk=car.pk)