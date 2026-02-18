from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label='Full Name :', help_text='Total length must be within 70 characters!', required=False, widget= forms.Textarea(attrs={'id' :'textname', 'class' : 'textclass', 'placeholder': 'Enter your full name'}))
    email = forms.EmailField(label='User Email', widget=forms.EmailInput)
    Age = forms.CharField(widget=forms.NumberInput)
    Birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    Appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [('L', 'Large'), ('M', 'Medium'), ('S', 'Small')]
    Size = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    Meal = [('C', 'Chicken'), ('P', 'Panir'), ('M', 'Mashroom')]
    Ingredients = forms.MultipleChoiceField(choices=Meal, widget=forms.CheckboxSelectMultiple)
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 10:
            raise forms.ValidationError('The name should be more than 10 chars')
        if '.com' not in valemail:
            raise forms.ValidationError('The email should contain .com')


def len_check(value):
    if len(value)<10:
        raise forms.ValidationError('The required filed should contain more than 10 instances')

class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='The name should be more than 10 chars')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(50, message="Age can't be more than 50"), validators.MinValueValidator(24, message="Age can't be less than 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message='File name should include pdf or png')])




    # File = forms.FileField()
    # email = forms.EmailField(label='User Email')
    # Age = forms.IntegerField()
    # Weight = forms.FloatField()
    # Balance = forms.DecimalField()
    # Check = forms.BooleanField()
    # Birthday = forms.DateField()
    # Appointment = forms.DateTimeField()
    # CHOICES = [('L', 'Large'), ('M', 'Medium'), ('S', 'Small')]
    # Size = forms.ChoiceField(choices = CHOICES)
    # SizesForMultiple = forms.MultipleChoiceField(choices=CHOICES)


class PasswordValidationProject(forms.Form):
    name = forms.CharField(label='Full Name :', widget=forms.TextInput, validators=[validators.MinLengthValidator(4, message='The name should contain more than 4 characters')])
    password = forms.CharField(label='Password :', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password :', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        valcfpass = self.cleaned_data['confirm_password']
        if valpass != valcfpass:
            raise forms.ValidationError("Passwords doesn't match!")