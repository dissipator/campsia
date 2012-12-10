from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Attendance(models.Model):
    semester = models.ForeignKey('course.Semester')
    division = models.ForeignKey('course.Division')
    subject = models.ForeignKey('course.Subject')
    time = models.DateTimeField(auto_now_add=True)
    students_absent = models.ManyToManyField('course.Student',null=True,blank=True)
    
    def __unicode__(self):
        return self.subject