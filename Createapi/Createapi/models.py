from django.db import models
from django.contrib.auth.models import User

class Login(models.Model):
    name=models.CharField(max_length=100)
    passs=models.CharField(max_length=100)
    class Meta:
        db_table='Createapi_Login'
    

