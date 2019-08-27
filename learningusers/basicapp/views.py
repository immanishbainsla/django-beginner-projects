from django.shortcuts import render
from basicapp.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html', context=None)

def register(request):
    registered = False
    if request.method == 'POST':
        userform = UserForm(data=request.POST)
        profileform = UserProfileInfoForm(data=request.POST)

        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = profileform.save(commit=False)
            profile.user = user
            registered = True

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
            else:
                print(userform.errors, profileform.errors)
        else:
            userform = UserForm()
            profileform = UserProfileInfoForm()

    return render(request, 'basicapp/registration.html', {'registered':registered, 'userform':UserForm, 'profileform':UserProfileInfoForm})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('You Are Logged In, NICE.')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active.')

        else:
            print('Someone tried to Login and Failed.')
            print('Username = {} and Password = {}'.format(username, password))
            return HttpResponse('Invalid LogIn details supplied.')

    else:
        return render(request, 'basicapp/login.html', context=None)
