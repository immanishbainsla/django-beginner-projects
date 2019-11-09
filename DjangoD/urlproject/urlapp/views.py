from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def appurlinfo(request):
    s = '<h1 style="text-align:center">My URL is localhost:8000/urlapp/test/</h1>'
    return HttpResponse(s)
