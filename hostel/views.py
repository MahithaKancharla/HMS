from django.shortcuts import render
from .models import StudentInfo

# Create your views here.


def index(request):
    return render(request, 'index.html')

def student_list(request):
    students = StudentInfo.objects.all()

    return render(request,'list.html',{'students':students})
