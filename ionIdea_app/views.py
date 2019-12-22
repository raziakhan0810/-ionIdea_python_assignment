import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ionIdea_app.models import Employee, DepartmentEmployee, Department, Title, Salary
from datetime import date, datetime

logger = logging.getLogger(__name__)


def calculate_year(given_date):
    today = date.today()
    return today.year - given_date.year - ((today.month, today.day) < (given_date.month, given_date.day))


class EmployeeHire(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        birth_date = request.data.get('birth_date')
        employee_id = request.data.get('employee_id')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        gender = request.data.get('gender')
        hire_date = request.data.get('hire_date')
        salary = request.data.get('salary')
        department = request.data.get('department')
        title = request.data.get('title')
        try:
            if Employee.objects.filter(emp_no=employee_id):
                logger.debug('Employee record is already in database.')
                return Response({'Message': 'Employee record is already in database.'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                if not Department.objects.filter(dept_name=department):
                    logger.debug('Department does not exist!')
                    return Response({'Message': 'Department does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

                department = Department.objects.get(dept_name=department)
                birth_date_ = datetime.strptime(birth_date, '%d/%m/%Y')
                hire_date_ = datetime.strptime(hire_date, '%d/%m/%Y')
                age = calculate_year(birth_date_)
                if age in range(18, 60):
                    employee = Employee.objects.create(
                        emp_no=employee_id,
                        birth_date=birth_date_,
                        first_name=first_name,
                        last_name=last_name,
                        gender=gender,
                        hire_date=hire_date_
                    )
                    employee.save()
                    employee_department = DepartmentEmployee.objects.create(
                        emp_no=employee,
                        dept_no=department,
                        from_date=hire_date_,
                        to_date=date.today()
                    )
                    employee_department.save()
                    title = Title.objects.create(
                        emp_no=employee,
                        title=title,
                        from_date=hire_date_,
                        to_date=date.today()
                    )
                    title.save()
                    salary = Salary.objects.create(
                        emp_no=employee,
                        salary=salary,
                        from_date=hire_date_,
                        to_date=date.today(),
                    )
                    salary.save()
                    return Response({'Success': 'Records inserted successfully!'}, status=status.HTTP_200_OK)
                else:
                    logger.debug('Employee is not eligible for work!')
                    return Response({'Message': 'Employee is not eligible for work!'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception('Error while hiring employee - {}'.format(e))
            return Response({'Message': 'Error while hiring employee - {}'.format(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class EligibleForHike(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        emp_no = request.query_params.get('employee_id')
        department_for_hike = ["Customer Service", "Development", "Finance", "Human Resources", "Sales"]
        title_for_hike = ["Senior Engineer", "Staff", "Engineer", "Senior Staff", "Assistant Engineer",
                          "Technique Leader"]
        try:
            if not Employee.objects.filter(emp_no__exact=int(emp_no)):
                logger.debug('Employee does not exist!')
                return Response({'Message': 'Employee does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                employee = Employee.objects.get(emp_no=int(emp_no))
                experience = calculate_year(employee.hire_date)
                age = calculate_year(employee.birth_date)
                employee_department = DepartmentEmployee.objects.get(emp_no=employee.emp_no)
                employee_title = Title.objects.get(emp_no=employee.emp_no)
                if employee_department.dept_no.dept_name not in department_for_hike or employee_title.title not in title_for_hike:
                    return Response({"hike": False}, status=status.HTTP_200_OK)
                elif experience <= 1 or age <= 20:
                    return Response({"hike": False}, status=status.HTTP_200_OK)
                elif employee.gender == 'M' and employee_title.title == 'Technique Leader':
                    return Response({"hike": False}, status=status.HTTP_200_OK)
                else:
                    if employee_title.title == 'Staff':
                        employee_title.title = 'Senior Staff'
                    elif employee_title.title == 'Assistant Engineer':
                        employee_title.title = 'Engineer'
                    elif employee_title.title == 'Engineer':
                        employee_title.title = 'Senior Engineer'
                    elif employee_title.title == 'Senior Engineer':
                        employee_title.title = 'Technique Lead'
                    elif employee_title.title == 'Technique Lead':
                        employee_title.title = 'Manger'
                    employee_title.save()
                    return Response({"hike": True, "designation": employee_title.title}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception('Error while getting employee for hike - {}'.format(e))
            return Response({'Message': 'Error while getting employee for hike - {}'.format(e)},
                            status=status.HTTP_400_BAD_REQUEST)
