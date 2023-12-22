from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from schoolapp.models import Department, Course
from .models import Admission

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('home')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home2')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def home2(request):
    departments = Department.objects.all()
    courses = Course.objects.all()
    if request.method == 'POST':
        # Fetch form data
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        address = request.POST['address']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        department_id = request.POST['department']
        course_id = request.POST['course']
        purpose = request.POST['purpose']

        # Save the form data into the Admission model
        admission = Admission(
            name=name,
            gender=gender,
            dob=dob,
            address=address,
            age=age,
            phone=phone,
            email=email,
            department_id=department_id,
            course_id=course_id,
            purpose=purpose
        )
        admission.save()

    return render(request, 'home2.html', {'departments': departments, 'courses': courses})

def logout(request):
    auth.logout(request)
    return redirect('schoolapp:home')