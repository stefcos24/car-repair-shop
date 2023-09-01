from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from domain.decorators import unauthenticated_user


@unauthenticated_user
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # check if user is authenticated
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login user
            login(request, user)
            return redirect("domain")

    context = {}

    return render(request, "domain/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("user_login")
