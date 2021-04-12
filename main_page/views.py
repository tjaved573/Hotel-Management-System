from django.shortcuts import render

def home(request):
    if "guest_login" in request.GET:
        print("the guest is trying to log in")

    return render(request, 'main_page/home.html', {})

def login(request, entity):
    context = {
        'entity': entity
    }
    return render(request, 'main_page/login.html', context)


# def guest(request):
#     pass

# def employee(request):
#     pass

# def admin(request):
#     pass
#
