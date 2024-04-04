from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def register(request):
    print("in view")
    print(request.body)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(username,password)

        if not username or not password or not confirm_password:
            return JsonResponse({'error': 'All fields are required'}, status=400)
        if password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return redirect('my-login')
    
    elif request.method == 'GET':
        return render(request, 'register.html')

    return JsonResponse({'error': 'Unsupported method'}, status=405)


# def register(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('my-login')

#     context = {'registerform': form}
#     # if request.method == 'POST':
#     #     username = request.POST['username']
#     #     password = request.POST['password']
#     #     confirm_password = request.POST['confirm_password']

#     #     # Check if passwords match
#     #     if password != confirm_password:
#     #         return render(request, 'register.html', {'error': 'Passwords do not match'})

#     #     # Create and save user object
#     #     user = CustomUser.objects.create(username=username, password=password)
#     #     user.save()

#     #     # Redirect to a success page or login page
#     #     # Assuming you have a login page with the name 'login'
#     #     return redirect('login')

#     return render(request, 'register.html', context=context)


# def my_login(request):
#     return render(request, 'my-login.html')


def my_login(request):
    if request.method == "POST":
        # check if user entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, "Incorrect Credentials, Try again")
            print("yes")
            return render(request, "my-login.html")
    return render(request, 'my-login.html')


def my_logout(request):
    logout(request)
    return redirect("/")


def dashboard(request):
    if request.user.is_anonymous:
        return redirect("/")

    if request.user.is_authenticated:
        username = request.user.username
        print(username)
        # return render(request, 'dashboard.html', {"username": username.upper()})
        profile = StudentInfo.objects.get(email=username)
        if profile is None: 
            profile = WardenInfo.objects.get(email=username)
        return render(request,'dashboard.html',{"username": profile.name.upper(),'student_profile':profile})

    

def student_list(request):
    students = StudentInfo.objects.all()

    return render(request,'list.html',{'students':students})

def warden_list(request):
    wardens = WardenInfo.objects.all()

    return render(request,'profile.html',{'wardens':wardens})

def vacancies(request):
    girls = Hostel.objects.get(hostel_type='girls_hostel')
    count1 = girls.capacity - girls.filled_seats_count
    print(count1)
    boys = Hostel.objects.get(hostel_type='boys_hostel')
    count2 = boys.capacity - boys.filled_seats_count
    print(count2)

    return render(request,'vacancy.html',{'count1':count1,'count2':count2})