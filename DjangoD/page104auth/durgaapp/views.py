from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def java_exams_view(request):
    return render(request, 'durgaapp/javaexams.html')

@login_required
def python_exams_view(request):
    return render(request, 'durgaapp/pythonexams.html')

@login_required
def aptitude_exams_view(request):
    return render(request, 'durgaapp/aptitudeexams.html')
