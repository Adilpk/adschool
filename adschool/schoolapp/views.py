from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Department


# Create your views here.
def index(request, d_slug=None):
    dept = Department.objects.all()
    d_page = None
    course = None
    if d_slug != None:
        d_page = get_object_or_404(Department, slug=d_slug)
        course = Course.objects.all().filter(department=d_page)
    else:
        course = Course.objects.all()
    return render(request, 'home.html', {'department': d_page, 'course': course})


def department_detail(request, d_slug):
    department = get_object_or_404(Department, slug=d_slug)
    courses = Course.objects.filter(department=department)
    return render(request, 'department_detail.html', {'department': department, 'courses': courses})


