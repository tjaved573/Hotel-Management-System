from django.shortcuts import render
from django.db import connection, transaction
from guest.models import Guest, Employee, Reservation, ReservationRoomRel, Room, Hotel, Feature, FeatureRoomRel

def home(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)

    context = {
        'employee_name': f"{employee.first} {employee.last}",
    }

    return render(request, 'employee/home.html', context)
