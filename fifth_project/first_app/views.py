from django.shortcuts import render
from . forms import StudentData, contactForm, PasswordValidationProject
# Create your views here.
def app(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select = request.POST.get('select')
        return render(request, 'index.html', {'name':name, 'email':email, 'select':select})
    else:
        return render(request, 'index.html')
def submit_form(request):
    # print(request.POST)
    return render(request, 'form.html')

# def DjangoForm(request):
#     if request.method == 'POST':
#         form = contactForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = form.cleaned_data['File']
#             with open('./first_app/upload/' + file.name, 'wb+') as destination:
#                 for chunk in file.chunks():
#                     destination.write(chunk)
#             print(form.cleaned_data)
#             return render(request, 'djangoform.html', {'form':form})
#     else:
#         form = contactForm()
#     return render(request, 'djangoform.html', {'form':form})

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'djangoform.html', {'form':form})
    else:
        form = contactForm()
    return render(request, 'djangoform.html', {'form':form})

def DjangoForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'djangoform.html', {'form':form})
    else:
        form = StudentData()
    return render(request, 'djangoform.html', {'form':form})


def PasswordValidation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'password.html', {'form':form})
    else:
        form = PasswordValidationProject()
    return render(request, 'password.html', {'form':form})