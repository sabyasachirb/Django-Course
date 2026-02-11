from django.shortcuts import render

# Create your views here.
def about(response):
    d = {'age':21, 'name':'Sabyasachi' , 'ls': [1,2,4], 'Courses': [
        {
            'name': 'Python',
            'Fees': 12000,
            'Duration': '12 months'
        },
        {
            'name': 'Django',
            'Fees': 6000,
            'Duration': '3 months'
        },
        {
            'name': 'C',
            'Fees': 1200,
            'Duration': '2 months'
        }

    ]}
    return render(response, 'navigation/about.html', d)

def contact(response):
    return render(response, 'navigation/contact.html')