from django.db import models,connection
from django import forms
from .models import *
from datetime import timedelta
from datetime import time
from datetime import date, datetime

# Create your models here.
class StudentInfo(models.Model):
    roll_no = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    joining_year = models.CharField(max_length=255)
    room_no = models.IntegerField()
    blood_group = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    address = models.TextField()
    gender = models.CharField(max_length=255,default=None)
    email = models.EmailField()
    father_name = models.CharField(max_length=255,null=True)
    father_contact_number = models.CharField(max_length=255,null=True)
    mother_name = models.CharField(max_length=255,null=True)
    mother_contact_number = models.CharField(max_length=255,null=True)
    guardian_name = models.CharField(max_length=255,null=True)
    guardian_contact_number = models.CharField(max_length=255,null=True)


    def  __str__(self):
        return self.roll_no

class WardenInfo(models.Model):
    name = models.CharField(max_length=255)
    joining_year = models.CharField(max_length=255)
    room_no = models.IntegerField()
    blood_group = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    ismale = models.BooleanField(default=False)
    isfemale = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return self.name