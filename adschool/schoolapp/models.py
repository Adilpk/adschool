from django.db import models

# Create your models here.
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'dept'
        verbose_name_plural = 'department'

    def get_url(self):
        return reverse('schoolapp:courses_by_department', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return '{}'.format(self.name)



