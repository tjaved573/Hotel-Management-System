from django.shortcuts import render
from main_page.models import Hotel, Reservation, Feature
from .forms import FeatureForm

# Create your views here.
#

def main_page(request):
    hotels = []
    reservations = []
    features = []
    if "list_hotels" in request.GET:
        for h in Hotel.objects.raw("SELECT * FROM hotel"):
            hotels.append(h)
    if "list_reservations" in request.GET:
        for r in Reservation.objects.raw("SELECT * FROM reservation"):
            reservations.append(r)
    if "list_features" in request.GET:
        for r in Feature.objects.raw("SELECT * FROM features"):
            features.append(r)
    if request.method == "POST":
        form = FeatureForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_feature = Feature(feature_id=cd['feature_id'], feature=cd['feature'], price=cd['price'], description=cd['description'])
            print(f"new featuer: {new_feature}")
        else:
            print("invalid form.")
    return render(request, 'main_page.html', {'hotels': hotels, 'reservations': reservations, 'features': features})
