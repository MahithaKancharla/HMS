from django.db import models, connection
from django import forms
from .models import *
from datetime import timedelta
from datetime import time
from datetime import date, datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


# Create your models here.


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']

# def __init__(self, *args, **kwargs):
#     super(CreateUserForm, self).__init__(*args, **kwargs)
#     self.fields['username'].widget.attrs.update(
#         {'placeholder': 'Username'})
#     # self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
#     # self.fields['password1'].widget.attrs.update(
#     #     {'placeholder': 'Password'})
#     self.fields['password2'].widget.attrs.update(
#         {'placeholder': 'Confirm Password'})

#     for field_name, field in self.fields.items():
#         field.help_text = ''


class StudentInfo(models.Model):
    roll_no = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    joining_year = models.CharField(max_length=255)
    room_no = models.IntegerField()
    blood_group = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    address = models.TextField()
    gender = models.CharField(max_length=255, default=None)
    email = models.EmailField()
    father_name = models.CharField(max_length=255, null=True)
    father_contact_number = models.CharField(max_length=255, null=True)
    mother_name = models.CharField(max_length=255, null=True)
    mother_contact_number = models.CharField(max_length=255, null=True)
    guardian_name = models.CharField(max_length=255, null=True)
    guardian_contact_number = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.roll_no


class WardenInfo(models.Model):
    name = models.CharField(max_length=255)
    joining_year = models.CharField(max_length=255)
    room_no = models.IntegerField()
    blood_group = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Hostel(models.Model):
    hostel_type = models.CharField(max_length=255, primary_key=True)
    hostel_name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    filled_seats_count = models.IntegerField()

    def __str__(self):
        return self.hostel_name


class Room(models.Model):
    room_no = models.CharField(max_length=5)
    member1_roll_no = models.ForeignKey(
        'StudentInfo', on_delete=models.CASCADE, related_name='member1_rooms')
    member2_roll_no = models.ForeignKey(
        'StudentInfo', on_delete=models.CASCADE, related_name='member2_rooms')
    vacant = models.BooleanField(default=False)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)

    def __str__(self):
        return self.room_no
