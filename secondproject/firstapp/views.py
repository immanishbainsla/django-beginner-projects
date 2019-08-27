from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    mydict = {'insertme':'HELLO i am from FIRSTAPP'}
    return render(request,'firstapp/index.html',context=mydict)

def home(request):
    return HttpResponse('<h1>Hello World.</h1><p>This is HomePage.</p>')
