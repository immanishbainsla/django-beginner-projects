from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# views goes here

def index(request):
    return render(request, 'index.html',{})


@login_required
def logout_view(request):
    return render(request, 'logout.html')
