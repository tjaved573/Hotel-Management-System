from django.shortcuts import render
from main_page.models import Hotel, Reservation
from .forms import ReservationForm

# Create your views here.
#

def main_page(request):
    hotels = []
    reservations = []
    if "list_hotels" in request.GET:
        for h in Hotel.objects.raw("SELECT * FROM hotel"):
            hotels.append(h)
    if "list_reservations" in request.GET:
        for r in Reservation.objects.raw("SELECT * FROM reservation"):
            reservations.append(r)
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, 'main_page.html', {'hotels': hotels, 'reservations': reservations})
