from django.shortcuts import render
from posts.models import Post
from categories.models import Category
def Home(request, category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = category)
    catergories = Category.objects.all()
    return render(request, 'home.html', {'data':data, 'catagory':catergories})