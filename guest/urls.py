from django.urls import path
from guest import views

urlpatterns = [
    path('', views.home, name='guest_home'),
    path('make-a-reservation/', views.make_reservation, name='make_a_reservation'),
]
