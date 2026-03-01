from django.contrib.auth.views import LogoutView
from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    # path('logout/', views.userlogout, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/edit/', views.update_profile, name='update_profile'),
    path('change-pass/', views.change_pass, name='change_pass'),
    path('profile/', views.profile, name='profile'),

]
