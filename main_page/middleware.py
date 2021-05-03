from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, request

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

