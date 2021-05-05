from django.shortcuts import render
from .forms import LoginForm

def home(request):
    if "guest_login" in request.GET:
        print("the guest is trying to log in")

    return render(request, 'main_page/home.html', {})

def login(request, entity):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            cd = form.cleaned_data
            print(f"username: {cd['username']}, password: {cd['password']}")
            form = LoginForm()
        else:
            print("invalid form.")
            if 'username' in form.errors:
                print("username missing")
            if 'password' in form.errors:
                print("password missing")

    context = {
        'entity': entity,
        'form': form
    }
    return render(request, 'main_page/login.html', context)


# def guest(request):
#     pass

# def employee(request):
#     pass

# def admin(request):
#     pass
#
