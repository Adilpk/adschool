from django.db import models
from schoolapp.models import Course, Department

# Create your models here.
class Admission(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=50)

    # Other fields as needed

    def __str__(self):
        return self.name
