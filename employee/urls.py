from django.urls import path
from employee import views

urlpatterns = [
    path('<employee_id>/', views.home, name='employee_home'),
    # path('make-a-reservation/<guest_id>/', views.make_reservation, name='make_a_reservation'),
]
