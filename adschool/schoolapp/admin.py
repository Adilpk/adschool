from django.contrib import admin
from .models import Department,Course
# Register your models here.
class DeptAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Department, DeptAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)