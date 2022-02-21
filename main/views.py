from django.shortcuts import render, redirect
from donateform.models import Donateform
from main.models import *
from .forms import *
from user.models import User
from user.forms import UserForm
from django.contrib import auth
from .import models, forms
# Create your views here.


def LoginRegister(request):
    if request.method == "POST":

        customers = CustomerForm(request.POST, request.FILES)

        customers.save()

        return redirect("/")

    return render(request, "LoginRegister.html")


def signin(request):
    if request.method == 'POST':
        donor_name = request.POST.get('donor_email')
        donor_password = request.POST.get('donor_password')
        user = Donor.objects.get(
            donor_email=donor_name, donor_password=donor_password)
        if user is not None:
            request.session['donor_email'] = user.donor_email
            return redirect("/index/")

    return render(request, "LoginRegister.html")


def loginadmin(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = User.objects.get(username=un, password=pw)
        if user is not None:
            request.session['username'] = request.POST['username']
            request.session['id'] = user.id

            return redirect('/user/dashboard/')

    else:
        return render(request, "AdminLogin.html")


def donate(request):
    return render(request, "donate.html")


def index(request):
    return render(request, "index.html")


def logout(request):
    request.session.flush()
    return redirect("/signin/")


def edit_profile_view(request):
    donor = Donor.objects.get(donor_email=request.session['donor_email'])
    return render(request, "edit_profile.html", {'donor': donor})


def update(request, c_id):
    donor = Donor.objects.get(donor_id=c_id)
    form = CustomerForm(request.POST, instance=donor)
    print(form)
    form.save()
    return redirect("/logout")


def delete(request, c_id):
    donor = Donor.objects.get(donor_id=c_id)
    donor.delete()
    return redirect("/")


def userdashboard(request):
    alldonation = Donateform.objects.all()
    return render(request, 'admindashboard.html', {'alldonation': alldonation})


def useredit(request):
    user = User.objects.get(id=request.session['id'])
    return render(request, "editadminprofile.html", {'user': user})


def userupdate(request, c_id):
    user = User.objects.get(id=c_id)
    form = UserForm(request.POST, instance=user)
    form.save()
    return redirect("/useredit")
