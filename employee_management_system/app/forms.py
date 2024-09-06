
from django import forms
from .models import Employee

class EmployeeCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'job_title', 'department', 'date_of_birth', 'date_of_hire', 'salary']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Passwords do not match')

        return cleaned_data

    def save(self, commit=True):
        employee = super().save(commit=False)
        if commit:
            employee.set_password(self.cleaned_data["password1"])
            employee.save()
        return employee
