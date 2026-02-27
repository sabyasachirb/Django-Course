
from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('profile/edit/', views.update_profile, name='update_profile'),
    path('change-pass/', views.change_pass, name='change_pass'),
    path('profile/', views.profile, name='profile'),

]
