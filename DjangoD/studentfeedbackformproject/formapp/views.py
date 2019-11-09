from django.shortcuts import render
from formapp import forms

# Create your views here.

def feedbackview(request):
    if request.method == 'POST':
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and printing information')
            print('Name:',form.cleaned_data['name'])
            print('Roll No:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('FeedBack:',form.cleaned_data['feedback'])
    else:
        form = forms.FeedBackForm()

    return render(request,'formapp/feedback.html',{'form':form})


def index(request):
    return render(request, 'formapp/index.html')
