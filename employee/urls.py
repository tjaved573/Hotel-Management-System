from django.urls import path
from employee import views

urlpatterns = [
    path('', views.home, name='employee_home'),
    path('all_hotels_info/', views.all_hotels_info, name='all_hotels_info'),
]
