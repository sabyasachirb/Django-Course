from django.shortcuts import render
from django_filters import DateTimeFilter
# Create your views here.
def app(res):
    dic = {
        'name' : 'Sabyasachi Roy Barman',
        'age' : 24,
        'Address' : ['997', 'East Medda', 'Brahmanbaria'],
        'lst': [1,2,3,4,5],
        'time': DateTimeFilter.
    }
    return render(res, 'app/app.html', dic)
def about(res):
    return render(res, 'app/about.html')
def contact(res):
    return render(res, 'app/contact.html')