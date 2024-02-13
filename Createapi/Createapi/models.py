from django.db import models

class Login(models.Model):
    name=models.CharField(max_length=100)
    passs=models.CharField(max_length=100)
    # class Meta:
    #     db_table='polls_Login'
    

