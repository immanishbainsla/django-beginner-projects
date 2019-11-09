from django.db import models
# import timezone
# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

    def __str__(self):
        # return f'Employee Object with eno : {self.eno}'
        return self.ename


class Job(models.Model):
    posting_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)
    offered_salary = models.FloatField()
    qualification = models.CharField(max_length=30)

    def __str__(self):
        return self.posting_date
