from django.shortcuts import render, redirect
from main.models import *
from .forms import *
# Create your views here.


def dform(request):
    print("hh")
    if request.method == "POST":

        customers = donatesForm(request.POST, request.FILES)

        customers.save()
        return redirect("/index/")

    return render(request, "donate.html",)


def index(request):
    return render(request, "index.html")
