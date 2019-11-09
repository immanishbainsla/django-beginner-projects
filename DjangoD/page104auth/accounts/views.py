from django.shortcuts import render
from django.http import HttpResponseRedirect
from accounts.forms import SignUpForm

# Create your views here.

def signupview(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'accounts/signup.html', {'form':form})

from django.contrib.auth.decorators import login_required

# @login_required
# def logout_view(request):
#     return render(request, 'logout.html')
