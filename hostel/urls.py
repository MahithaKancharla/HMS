from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("register", views.register, name='register'),
    path("my-login", views.my_login, name='my-login'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("my-logout", views.my_logout, name='my-logout'),
    path("list/", views.student_list, name='student_list'),
    # path("profile/",views.userprofile,name='userprofile'),
]
