
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("author/", include('author.urls')),
    path("category/", include('categories.urls')),
    path("category/<slug:category_slug>/", views.Home, name = 'categorywisepost'),
    path("posts/", include('posts.urls')),
    path("", views.Home, name="Home")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
