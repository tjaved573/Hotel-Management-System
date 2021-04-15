from django.shortcuts import render


def home(request, guest_id):
    return render(request, 'guest/home.html', {'guest_id': guest_id})
