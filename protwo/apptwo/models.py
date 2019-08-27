from django.db import models

# Create your models here.
class users(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(max_length=128,unique=True)
