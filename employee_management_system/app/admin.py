from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job_title', 'department', 'email', 'date_of_hire')
    search_fields = ('first_name', 'last_name', 'job_title', 'department', 'email')
