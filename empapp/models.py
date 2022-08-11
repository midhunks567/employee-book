from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=200,unique=True,null=False)
    emp_id=models.IntegerField(unique=True,null=False)
    occup=models.CharField(max_length=200,null=False)