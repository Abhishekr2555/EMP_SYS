from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Role, Department,cursol,about_photo
from datetime import datetime
from django.contrib import messages
import pandas as pd
from django.http import JsonResponse
# Create your views here.


def index(request):
    # return HttpResponse("About")
    return render(request, "index.html")


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        salary = request.POST.get('salary', '')
        bonus = request.POST.get('bonus', '')
        phone = request.POST.get('phone', '')
        # Assuming dept is a department ID
        dept_id = request.POST.get('dept', '')
        role_id = request.POST.get('role', '')  # Assuming role is a role ID
        hire_date_str = request.POST['hire_date']
        hire_date = datetime.strptime(hire_date_str, '%Y-%m-%d').date()
        location = request.POST.getlist('location')
        # Validate input
        if salary and bonus and phone:
            try:
                salary = float(salary)
                bonus = float(bonus)
                phone = int(phone)

                # Get department and role objects
                department = Department.objects.get(id=dept_id)
                role = Role.objects.get(id=role_id)

                new_emp = Employee(
                    first_name=first_name,
                    last_name=last_name,
                    salary=salary,
                    bonus=bonus,
                    phone=phone,
                    dept=department,
                    role=role,
                    hire_date=hire_date

                )
                new_emp.save()
                return HttpResponse('Employee added Successfully')
            except (ValueError, Department.DoesNotExist, Role.DoesNotExist):
                return HttpResponse('Invalid input or foreign key does not exist.')

        return HttpResponse('Please provide all required fields.')

    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception Occurred! Employee Has Not Been Added')


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_rmv = Employee.objects.get(id=emp_id)
            emp_rmv.delete()
            messages.success(request, 'Employee removed successfully.')
            return redirect('index')
        except Employee.DoesNotExist:
            messages.error(request, 'Employee does not exist.')
            return redirect('index')
    emps = Employee.objects.all()
    data = {
        'emps': emps
    }
    return render(request, 'remove.html', data)


def filter_emp(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        salary = request.POST.get('salary')
        phone = request.POST.get('phone')

        emps = Employee.objects.all()
        if phone:
            emps = emps.filter(phone__icontains=phone)
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        data = {
            'emps': emps
        }
        if emps:
            return render(request, 'view_all_emp.html', data)
        else:
            return HttpResponse('Not Found')

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    return HttpResponse('Not Found')


def d_emp(request):
    # return HttpResponse('Not Found')
    employees = Employee.objects.all()
    # Create a Pandas DataFrame with the employee data
    data = []
    for employee in employees:
        department = employee.dept if employee.dept else ''
        data.append({"First Name": employee.first_name,
                     "Last Name": employee.last_name,
                    "Department": department, 
                    "Salary": employee.salary,
                    "Bonus":employee.bonus,
                    "Phone Number":employee.phone,
                    "Role":	employee.role,
                    "Hiredate":employee.hire_date
                    })
    pd.DataFrame(data).to_excel('Employees_details.xlsx')

    return JsonResponse({'status': 200})

def home(request):
    obj=cursol.objects.all()
    data={
        'obj':obj
    }
    return render(request,'home.html',data)

def login(request):
    return render(request,'login.html')

def signin(request):
    return render(request,'signin.html')
def contect(request):
    return render(request,'contect.html')

def about(request):
    obj=about_photo.objects.all()
    print("Number of instances retrieved:", len(obj))  
    data={
        'obj1':obj
    }
    return render(request,'about.html',data)