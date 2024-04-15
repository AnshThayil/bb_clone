from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField()
    first_name = forms.CharField(required=True, max_length=150)
    last_name = forms.CharField(required=True, max_length=150)

    class Meta:
        model = User
        fields = (
            'username', 
            'is_staff',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
