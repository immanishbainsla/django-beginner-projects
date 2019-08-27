from django.shortcuts import render
from django.http import HttpResponseRedirect
# from apptwo.models import users
from django.contrib import messages
from apptwo.forms import NewUserForm
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def user(request):
    # userlist = users.objects.order_by('firstname')
    # userdict = {'users':userlist}
    # return render(request,'apptwo/users.html', context=userdict)
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'We have recieved your Data! Thanks for Trying.')
            return HttpResponseRedirect(reverse('index'))
        else:
            print('ERROR FORM INVALID.')

    return render(request, 'apptwo/users.html', {'form':form})


# def help(request):
#     helpdict = {'helpinsert':'HELP PAGE'}
#     return render(request,'apptwo/help.html',context=helpdict)
