from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class College(models.Model):
    api_secret = models.CharField(max_length=50,null=True,blank=True)
    api_user = models.CharField(max_length=50,null=True,blank=True)
    api_host = models.CharField(max_length=255,null=True,blank=True)
    erp_table_id = models.IntegerField(null=True,blank=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name

#users - student Profile Fields     

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #students division ID , later use this fetch the attendance through XMLRPC
    division_id = models.IntegerField(null=True,blank=True)
    #department
    department_id = models.IntegerField(null=True,blank=True)
    #college's ID, fetch other details through ID 
    college_id = models.IntegerField(null=True,blank=True)
    
    def __unicode__(self):
        return self.user
    
    

