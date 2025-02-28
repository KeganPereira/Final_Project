from django.db import models  

from django.contrib.auth.models import AbstractUser, AbstractBaseUser 


# Create your models here. 
class Custom(AbstractUser): 
      username = models.CharField(max_length=200, unique=True) 
      password= models.CharField(max_length=200) 
      points= models.IntegerField(default=0) 
      address= models.CharField(max_length=200,blank = False) 
      phone = models.CharField(max_length= 200 , blank =False) 



