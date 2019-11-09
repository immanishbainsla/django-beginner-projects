from django import forms

# Forms goes here

class LoginForm(forms.Form):
    name = forms.CharField()
    roll = forms.IntegerField()
