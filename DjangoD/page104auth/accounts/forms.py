from django import forms
from django.contrib.auth.models import User

# Form goes here

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
