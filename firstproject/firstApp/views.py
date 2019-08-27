from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Topic,Webpage,AccessRecoed

# Create your views here.

def index(request):
    webpageslist = AccessRecoed.objects.order_by('date')
    date_dict = {'access_record':webpageslist}
    # my_dict = {'insertme':'Hello I am from VIEWS.PY','name':'Manish Bainsla'}
    return render(request,'firstApp/index.html',context=date_dict)
