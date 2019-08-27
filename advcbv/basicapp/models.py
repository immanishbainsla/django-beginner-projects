from django.db import models
from django.urls import reverse

# Create your models here.

class school(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basicapp:detail',kwargs={'pk':self.pk})

class student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(school, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
