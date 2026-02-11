from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    dic = {'name':'Sabyasachi Roy Barman', 'age': 24, 'lst':['amar', 'Nam', 'Sabyasachi'],
           'empt': "",
           'bday': datetime.datetime.now(),
           'chutodic': {
               'chuto' : 'chul',
               'maturity': 'nai',
               'biye':'unmarried'
           }}
    return render(request, "app/home.html", dic)