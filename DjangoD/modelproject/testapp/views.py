from django.shortcuts import render
from testapp.models import Employee
# Create your views here.

def empdata(request):
    emp_list = Employee.objects.all()
    context = {'emp_list':emp_list}
    return render(request, 'testapp/emp.html', context)
