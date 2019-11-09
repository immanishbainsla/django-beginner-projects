from django.contrib import admin

from .models import Employee, Job

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Job)
