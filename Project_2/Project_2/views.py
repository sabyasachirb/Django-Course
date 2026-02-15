from django.shortcuts import render

def Home(res ):
    return render(res, 'home.html')