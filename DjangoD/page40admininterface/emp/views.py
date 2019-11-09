from django.shortcuts import render
from .models import Employee, Job



# Create your views here.

def empdata(request):
    emp_list = Employee.objects.all()
    context = {'emp_list':emp_list}
    return render(request, 'emp/emp.html', context)
