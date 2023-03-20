from django.db import models
class student(models.Model):        #models is module and Model is used for database
    Name=models.CharField(max_length=120)
    City=models.CharField(max_length=50)
# Create your models here.
