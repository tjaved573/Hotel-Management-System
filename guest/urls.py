from django.urls import path
from guest import views

urlpatterns = [
    path('<guest_id>/', views.home, name='guest_home'),
]
