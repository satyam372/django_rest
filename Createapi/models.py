from django.db import models
from django.contrib.auth.models import User


class Login(models.Model):
    name=models.CharField(max_length=100)
    passs=models.CharField(max_length=100)
    class Meta:
        db_table='Createapi_Login'

# made above table for authentication but used django default table

class Raisecomplaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    emp_id=models.IntegerField()
    department=models.CharField(max_length=100)
    problem=models.CharField(max_length=100)
    sub_problem=models.CharField(max_length=100)
    engineer=models.CharField(max_length=100)
    
    class Meta:
        db_table='Raisecomplaint'

##  refer database schema for better understanding of models.
class Raisecomplaint_2(models.Model):
    complaint=models.ForeignKey(Raisecomplaint,on_delete=models.CASCADE,primary_key=True)
    # in the above line we have column called complaint
    # but it is complaint_id in mysql database 
    # but still it was able to send data from postman without making any field error
    # but how??
    # the reason is that when we create a an foreign_key relation in django , it by default attaches or creates "id" word
    # that's we are writing only word "complaint" but in backend/logic it is "complaint_id"

    # for testing this api with postman send data in the form of (form-data)


    #  "complaint=models.ForeignKey(Raisecomplaint,on_delete=models.CASCADE,primary_key=True)"

      #   in the above statement when we were not using (primary_key=True) we were geeting
      #   the error as operational error as Raisecomplaint_2.id not present in field list
      #   this was because by default django behaverly expects primary key when we
      #   create model or establish a foreign key relationship in model
      #   till we dont explictly tell django that our primary key name is different 
      #   till then it will expect primary key as id
      #   that's why we added a statement (primary_key=True)

    

    descrp=models.CharField(max_length=100)
    priority=models.CharField(max_length=100)
    photo_of_issue=models.ImageField(upload_to='media/images', default=None)
    floor=models.CharField(max_length=50)
    
    # changed path to 'media/images' this is the actuall directory name 
    # which is made in django project file

    class Meta:
        db_table='Raisecomplaint_2'


    

