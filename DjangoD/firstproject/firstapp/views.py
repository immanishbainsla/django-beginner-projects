from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    s = '<h1 style="text-align:center">Hello, this is HomePage</h1>'
    return HttpResponse(s)
