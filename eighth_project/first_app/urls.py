from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.Home, name='Homepage'),
    path('signup/',views.Signup, name='Signup'),
    path('profile/',views.profile, name='profile'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('passchange/',views.pass_change, name='passchange'),
    path('passchange2/',views.pass_change2, name='passchange2'),
]
