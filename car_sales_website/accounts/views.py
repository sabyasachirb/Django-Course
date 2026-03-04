from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from . forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/register.html', {'form': form})
    
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class LogoutView(LoginRequiredMixin, View):
    def post(self, request):
        logout(request)
        return redirect('home')
    
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        orders = request.user.order_set.all().order_by('-order_date')
        return render(request, 'accounts/profile.html', {'form': form, 'orders': orders})
    
    def post(self, request):
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        orders = request.user.order_set.all().order_by('-order_date')
        return render(request, 'accounts/profile.html', {'form': form, 'orders': orders})