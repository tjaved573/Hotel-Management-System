from django.shortcuts import render
from main_page.models import Hotel

# Create your views here.
#

def main_page(request):
    if "list_hotels" in request.POST:
        hotels = []
        for h in Hotel.objects.raw("SELECT * FROM hotel"):
            hotels.append(h)
        return render(request, 'main_page.html', {'hotels': hotels})    
    return render(request, 'main_page.html', {})
