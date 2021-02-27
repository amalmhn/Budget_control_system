from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User #this is a built in model
        fields = ['first_name' , 'last_name' , 'username' , 'email' , 'password1' , 'password2']

