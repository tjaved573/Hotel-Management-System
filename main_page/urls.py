from django.urls import path, include
from main_page import views
from guest import views as guest_views

urlpatterns = [
    path('', views.home, name='main_page_home'),
    # path('guest/', guest_views.home, name='guest_home')
]
