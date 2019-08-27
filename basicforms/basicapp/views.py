from django.shortcuts import render
from basicapp import forms

# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def formnameview(request):
    

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # do something
            print('VALIDATION SUCCESS.')
            print('NAME : '+form.cleaned_data['name'])
            print('EMAIL : '+form.cleaned_data['email'])
            print('TEXT : '+form.cleaned_data['text'])
    form = forms.FormName()       


    return render(request, 'basicapp/form_page.html', {'form':form})
