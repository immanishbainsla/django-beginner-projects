from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    return render(request, 'accounts/home.html')


@login_required
def Java_exams_view(request):
    return render(request, 'accounts/javaexams.html')


@login_required
def python_exams_view(request):
    return render(request, 'accounts/pythonexams.html')


@login_required
def aptitude_exams_view(request):
    return render(request, 'accounts/aptitudeexams.html')


@login_required
def logout_view(request):
    return render(request, 'accounts/logout.html')
