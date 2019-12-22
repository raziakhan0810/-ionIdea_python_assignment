from django.db import models


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    emp_no = models.IntegerField()
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hire_date = models.DateField()

    def __str__(self):
        return str(self.emp_no)


class Department(models.Model):
    dept_no = models.CharField(max_length=4)
    dept_name = models.CharField(max_length=40)

    def __str__(self):
        return self.dept_no


class DepartmentEmployee(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dept_no = models.ForeignKey(Department, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()


class Title(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()


class Salary(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
