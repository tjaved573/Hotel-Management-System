from django.urls import path
from guest import views

urlpatterns = [
    path('<guest_id>/', views.home, name='guest_home'),
    path('make-a-reservation/<guest_id>/', views.make_reservation, name='make_a_reservation'),
]
