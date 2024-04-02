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

    def  __str__(self):
        return self.roll_no
