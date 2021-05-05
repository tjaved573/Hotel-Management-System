"""hotel_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from guest import views as guest_views
from employee import views as employee_views

urlpatterns = [
    path('admin/', admin.site.urls, name="adminP"),
    path('', include('main_page.urls'), name='main'),
    path('guest/', include('guest.urls'), name='guest'),
    path('guest_register/', guest_views.registerUser, name="guest_register"),
    path('guest_login/', guest_views.loginUser, name="guest_login"),
    path('guest_logout/', guest_views.logoutUser, name="guest_logout"),

    path('employee/', include('employee.urls'), name='employee'),
    path('employee_register/', employee_views.registerUser, name="employee_register"),
    path('employee_login/', employee_views.loginUser, name="employee_login"),
    path('employee_logout/', employee_views.logoutUser, name="employee_logout"),
]
