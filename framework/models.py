from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 25)
    registration_date = models.DateField(default = datetime.date(2017,1,1))
    graduation_date = models.DateField(default = datetime.date(2017,1,1))
    
    
    def __str__ (self):
        
        return self.name