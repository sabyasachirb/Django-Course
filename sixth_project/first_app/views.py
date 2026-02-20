from django.shortcuts import render, redirect
from . import models
from first_app.forms import StudentForm
# Create your views here.
def Home(request):
    if request.method == 'POST':
        stndnt = StudentForm(request.POST)
        if stndnt.is_valid():
            stndnt.save()
            print(stndnt.cleaned_data)
    else:
        stndnt = StudentForm()
    return render(request, 'index.html', {'data':stndnt})


def delete_student(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("Student")

def Student(request):
    student = models.Student.objects.all()
    return render(request, 'student.html', {'data':student})