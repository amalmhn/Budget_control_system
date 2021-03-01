from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.admin.widgets import AdminDateWidget


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User #this is a built in model
        fields = ['first_name' , 'last_name' , 'username' , 'email' , 'password1' , 'password2']


class ExpenseCreateForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class DateSearchForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget())

