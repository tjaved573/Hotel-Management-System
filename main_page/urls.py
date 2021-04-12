from django.urls import path
from main_page import views

urlpatterns = [
    path('', views.home, name='main_page_home'),
    path('login/<entity>/', views.login, name='login'),
    # path('guest', views.guest, name='main_page_guest'),
    # path('employee', views.employee, name='main_page_employee'),
    # path('admin', views.admin, name='main_page_admin'),
]
