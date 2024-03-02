from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Role, Department, cursol, about_photo1, about_photo2, about_photo3, User, Website, Contact
from datetime import datetime
from django.contrib import messages
import pandas as pd
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
import random
from twilio.base.exceptions import TwilioRestException

from django.conf import settings
from django.core import mail
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def home(request):
    obj = cursol.objects.all()
    data = {
        'obj': obj
    }
    return render(request, 'home.html', data)


@login_required(login_url='login')
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
                return render(request, 'index.html')
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
                     "Bonus": employee.bonus,
                     "Phone Number": employee.phone,
                     "Role":	employee.role,
                     "Hiredate": employee.hire_date
                     })
    pd.DataFrame(data).to_excel('Employees_details.xlsx')

    return JsonResponse({'status': 200})


@login_required(login_url='login')
def contect(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        descrp = request.POST.get('message')
        qry = Contact(name=fname, email=email,
                      subject=subject, description=descrp)
        qry.save()

        # ---Email Sending Here
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_msg = mail.EmailMessage(f'Email From {fname}', f'UserEmail:{email}\n\nMesseage:{descrp}', from_email=[
                                      'name@gmail.com'], connection=connection)
        email_client = mail.EmailMessage('Svarnim Managament Teams Custmor', request.POST.get(
            'message'), from_email, [email], connection=connection)

        # mail.send_mail(
        #     'Customer Support Request',
        #     f'Customer Name: {fname}\nCustomer Email: {email}\nMessage: {descrp}\nCompany Website: http://www.yourcompany.com',
        #     'name@gmail.com',
        #     ['name8@gmail.com'],
        #     fail_silently=False,
        # )

        connection.send_messages([email_msg, email_client])
        connection.close()
        return redirect('contect')

    return render(request, 'contect.html')


def about(request):
    obj1 = about_photo1.objects.all()
    obj2 = about_photo2.objects.all()
    obj3 = about_photo3.objects.all()
    data = {
        'about1': obj1,
        'about2': obj2,
        'about3': obj3,
    }
    return render(request, 'about.html', data)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('username ans password incorrect')
    return render(request, 'login.html')


def sign(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')

        if password != cpassword:
            return HttpResponse('password not matched')
        else:
            my_user = User.objects.create_user(uname, email, password)
            my_user.save()
            return redirect('login')

        # print(uname,email,password,cpassword)
    #     return redirect('login')
    return render(request, 'signup.html')


def logoutpage(request):
    logout(request)
    return redirect('login')


def login1(request):
    if request.method == 'POST':
        if request.method == 'POST':
            mobile = request.POST.get('mobile')
            if mobile:
                otp = str(random.randint(1000, 9999))

            # Save the generated OTP in the user's session or database for verification

                account_sid = 'xxxx'
                auth_token = 'xxxx'
                twilio_mobile = 'xxxx'

                client = Client(account_sid, auth_token)
                try:
                    message = client.messages.create(
                        body=f'Your OTP is: {otp}',
                        from_=twilio_mobile,
                        to=mobile
                    )
                    # return redirect('otp')
                    return render(request, 'otp.html')
                except TwilioRestException as e:
                    return JsonResponse({'error': f'Twilio error: {e.msg}', 'code': e.code}, status=500)
            else:
                return JsonResponse({'error': 'Invalid phone number.'})

    return render(request, 'login1.html')


def qrcode(request):
    name = 'Further more Info'
    obj = Website.objects.get(id=1)
    contxt = {
        'name': name,
        'obj': obj
    }
    return render(request, 'qrcode.html')


def otp(request):
    mobile = request.session.get('mobile')

    if not mobile:
        # Redirect to the phone number entry form if no mobile number is stored in the session
        return redirect('login1')

    if request.method == 'POST':
        otp_entered = request.POST.get('otp')

        # Retrieve the OTP associated with the phone number from the database
        # Save the mobile number in the session
        request.session['mobile'] = mobile

        # Generate OTP
        if otp_entered == {otp}:  # Compare the entered OTP with the one in the database
            # Redirect to the dashboard or any other page
            return redirect('home')
        else:
            return HttpResponse('Invalid OTP!')

    return render(request, 'otp.html')
