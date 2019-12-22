from django.contrib import admin

from ionIdea_app.models import Employee, Department, DepartmentEmployee, Title, Salary


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'dept_no', 'dept_name')


@admin.register(DepartmentEmployee)
class DepartmentEmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_no', 'dept_no', 'from_date', 'to_date')


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_no', 'title', 'from_date', 'to_date')


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_no', 'salary', 'from_date', 'to_date')
