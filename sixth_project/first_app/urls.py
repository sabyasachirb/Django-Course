from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home, name='Home'),
    path('delete/<int:roll>', views.delete_student, name='Delete_student'),
    path('student/', views.Student, name='Student')
]
