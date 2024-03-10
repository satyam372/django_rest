from django.db import models
from django.contrib.auth.models import User


class Login(models.Model):
    name=models.CharField(max_length=100)
    passs=models.CharField(max_length=100)
    class Meta:
        db_table='Createapi_Login'

# made above table for authentication but used django default table

from django.db import models

class Raisecomplaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField()
    department = models.CharField(max_length=100)
    problem = models.CharField(max_length=100)
    sub_problem = models.CharField(max_length=100)
    engineer = models.CharField(max_length=100)

    class Meta:
        db_table = 'Raisecomplaint'

class Raisecomplaint_2(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    emp_id=models.CharField(max_length=100)
    descrp = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    photo_of_issue = models.ImageField(upload_to='media/images', default=None)
    floor = models.CharField(max_length=50)

    class Meta:
        db_table = 'Raisecomplaint_2'

    
    # changed path to 'media/images' this is the actuall directory name 
    # which is made in django project file

   

    
