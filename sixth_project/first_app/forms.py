from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Full Name ',
            'roll' : 'Student Roll',
        }
        # widgets = {
        #     'roll' : forms.PasswordInput(),
        #     'name' : forms.TextInput(attrs={'class' : ' btn btn-danger'})
        # }
        help_texts = {
            'name' : 'Write your full Name!'
        }
        error_messages = {
            'name' : {'required' : ' Your name is required!'}
        }