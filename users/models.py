from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Level(models.Model):
    shortname = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.shortname
    
class College(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name

class User(models.Model):
    level = models.ForeignKey(Level)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    college = models.ForeignKey(College)
    join_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
    

