from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from posts.models import Post
# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully!!')
            return redirect("login")
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'add_author.html', {'form':register_form, 'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass )
            if user is not None:
                messages.success(request, "Logged in successfully")
                login(request, user)
                return redirect('Home')
        else:
            messages.warning(request, 'Login information is incorrect!')
            return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request, 'add_author.html', {'form':form, 'type':'Login'})
    

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Password Updated Successfully!")
            update_session_auth_hash(request, user)
            return redirect('edit_profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_pass.html', {'form':form})

@login_required
def profile(request):
    form = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'form':form})

@login_required
def userlogout(request):
    logout(request)
    return redirect('Home')