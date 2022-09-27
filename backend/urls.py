from django.urls import path
from backend import views

urlpatterns = [
    path('register/', views.registerEmployee, name='user-register'),
    path('', views.getEmployees, name="users"),
    path('<str:pk>/', views.getEmployeeById, name='user'),

]