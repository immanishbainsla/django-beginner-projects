from django import forms

def starts_with_d(value):
    if value[0].lower() != 'd':
        raise forms.ValidationError('Name should be starts with d | D')

class FeedBackForm(forms.Form):
    name = forms.CharField(validators=[starts_with_d])
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        inputname=self.cleaned_data['name']
        print('validating name')
        if len(inputname) < 4:
            raise forms.ValidationError('The Minimum no of characters in the name field shouldbe 4')
        return inputname+'durga'

    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        print('Validating rollno field')
        return inputrollno

    def clean_email(self):
        inputemail=self.cleaned_data['email']
        print('Validating email field')
        return inputemail

    def clean_feedback(self):
        inputfeedback=self.cleaned_data['feedback']
        print('Validating feedback field')
        return inputfeedback
