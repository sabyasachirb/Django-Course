
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("author/", include('author.urls')),
    path("category/", include('categories.urls')),
    path("posts/", include('posts.urls')),
    path("profile/", include('profiles.urls')),
    path("", views.Home, name="Home")

]
