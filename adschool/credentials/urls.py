from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login',views.login,name='login'),
    path('home2',views.home2,name='home2'),

]
