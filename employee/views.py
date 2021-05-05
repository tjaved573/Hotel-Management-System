from django.shortcuts import render, redirect
from django.db import connection, transaction
from guest.models import Guest, Employee, Reservation, ReservationRoomRel, Room, Hotel, Feature, FeatureRoomRel
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


EMPLOYEE_PREFIX="employee/"


def registerUser(request):
    form = CreateUserForm(request.POST)
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            first = form.cleaned_data.get('firstname')
            last = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            hotel_id = form.cleaned_data.get('hotel_id')
            auth_user = User(username=f"{EMPLOYEE_PREFIX}{username}", email=email)
            auth_user.set_password(password)    # Does the hashing
            auth_user.save()

            employee_ids = [employee.employee_id for employee in Employee.objects.all()]
            available_ids = [1] if (employee_ids==None or len(employee_ids) == 0) else [e_id for e_id in range(1, max(employee_ids)+2) if e_id not in employee_ids]
            next_employee_pk = available_ids[0]
            e = Employee(
                employee_id = next_employee_pk,
                username    = username,
                hotel_id    = hotel_id,
                first       = first,
                last        = last,
            )
            e.save()        

            user = EMPLOYEE_PREFIX + username
            messages.success(request, 'Account successfully created for ' + user)
            return redirect('employee_login')

    context = {'form': form}

    return render(request, 'employee/register.html', context)


def loginUser(request):
    if(request.method =='POST'):            # if form has been submitted
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=f"{EMPLOYEE_PREFIX}{username}", password=password)
        if(user is not None):
            e_id = Employee.objects.all().filter(username=username)[0].employee_id
            print('valid user ' + str(e_id) + username)
            login(request, user)

            # TODO :find id against username, from local db and add here
            return redirect('employee_home')

    context = {}

    return render(request, 'employee/login.html', context)


def logoutUser(request):
    logout(request)
    context = {}

    return redirect('employee_login')


def home(request):
    username = request.user.username
    username = username.split(EMPLOYEE_PREFIX)[1]   # VERY IMPORTANT!!! "employee/username" becomes "username"
    employee_id = Employee.objects.get(username=username).employee_id
    employee = Employee.objects.get(employee_id=employee_id)

    hotel = Hotel.objects.get(hotel_id=employee.hotel_id)

    paying_customers = []

    with connection.cursor() as cursor:
        cursor.execute('SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED')
    try:
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.callproc('PayingCustomers', [hotel.hotel_id])
            results = cursor.fetchall()

            for row in results:
                paying_customers.append(row)
                # print(f"\033[94m{first_name} {last_name} {total}\033[0m")
    except IntegrityError:
        print("There was an integrity error")

    context = {
        'employee_name': f"{employee.first} {employee.last}",
        'hotel': hotel,
        'paying_customers': paying_customers,
    }

    return render(request, 'employee/home.html', context)


def all_hotels_info(request):
    username = request.user.username
    username = username.split(EMPLOYEE_PREFIX)[1]   # VERY IMPORTANT!!! "employee/username" becomes "username"
    employee_id = Employee.objects.get(username=username).employee_id
    employee = Employee.objects.get(employee_id=employee_id)

    hotel = Hotel.objects.get(hotel_id=employee.hotel_id)

    context = {
        'employee_name': f"{employee.first} {employee.last}",
        'hotel': hotel,
    }

    return render(request, 'employee/all_hotels_info.html', context)

