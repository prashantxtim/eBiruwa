from django.shortcuts import render

# Create your views here.


def LoginRegister(request):
    return render(request, "LoginRegister.html")


def AdminLogin(request):
    return render(request, "AdminLogin.html")


def donate(request):
    return render(request, "donate.html")


def index(request):
    return render(request, "index.html")
