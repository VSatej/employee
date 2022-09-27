from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name', 'email', 'phone_no', 'is_active')
    list_filter = ("username",)
    search_fields = ['username']

admin.site.register(Employee, EmployeeAdmin)