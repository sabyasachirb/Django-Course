from django.shortcuts import render

# Create your views here.
def about(res):
    return render(res, 'about.html')