from django.urls import path
from . import views
app_name= 'schoolapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('department/<slug:d_slug>/', views.department_detail, name='department_detail'),

]
