from django.db import models
import datetime
from django.utils import timezone
class Base(models.Model):  
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name    
        
    class Meta:
        abstract = True
    
class Student(Base):
    department = models.ForeignKey('Department')
    semester = models.ForeignKey('Semester')
    division = models.ForeignKey('Division')
    parent = models.ForeignKey('Parent')
    
class Parent(Base):
    office = models.CharField(max_length=20);

class Teacher(Base):
    department = models.ForeignKey('Department')
    
    
class Department(models.Model):
    name = models.CharField(max_length = 100)
    head = models.OneToOneField('Teacher',null=True,blank=True,related_name='head_of')
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name    
    
class Semester(models.Model):
    name = models.CharField(max_length = 100)
    duration = models.PositiveIntegerField()
    next_semester = models.OneToOneField('Semester',null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    subjects = models.ManyToManyField('Subject',null=True,blank=True)
    
    def __unicode__(self):
        return self.name    

class Division(models.Model):
    name = models.CharField(max_length = 100)
    semester = models.ForeignKey(Semester)
    department = models.ForeignKey(Department)
    current_capacity = models.PositiveIntegerField()
    max_capacity = models.PositiveIntegerField()
    next_division = models.OneToOneField('Division',null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey('Teacher',null=True,blank=True)
    def is_full(self):
        return self.max_capacity < self.current_capacity
    
    def __unicode__(self):
        return self.name   

class Subject(models.Model):
    name = models.CharField(max_length = 100)
    shortname = models.CharField(max_length = 10)
    max_marks = models.PositiveIntegerField()
    hours_per_week = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.name 
    

 
