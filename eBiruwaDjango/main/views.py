from django.shortcuts import render,redirect
from main.models import *
from .forms import *
from django.contrib.auth.models import User
from .import models, forms
# Create your views here.


def LoginRegister(request):
    if request.method=="POST":

        customers=CustomerForm(request.POST,request.FILES)
    

        customers.save()
        
        return redirect("/index/")
        
    return render(request,"LoginRegister.html")
 

def signin(request):
    if request.method=='POST':
        donor_name=request.POST.get('donor_email')
        donor_password=request.POST.get('donor_password')
        user=Donor.objects.get(donor_email=donor_name,donor_password=donor_password)
        if user is not None:
            request.session['donor_email']=user.donor_email
            return redirect("/index/")

    return render (request,"LoginRegister.html")


def AdminLogin(request):
    return render(request, "AdminLogin.html")


def donate(request):
    return render(request, "donate.html")


def index(request):
    return render(request, "index.html")

def logout(request):
    request.session.flush()
    return redirect("/signin/")

def edit_profile_view(request):
    donor=Donor.objects.get(donor_email= request.session['donor_email'])
    return render(request, "edit_profile.html", {'donor' : donor})

def update(request,c_id):
    donor=Donor.objects.get(donor_id=c_id)
    form = CustomerForm(request.POST, instance=donor)
    print(form)
    form.save()
    return redirect( "/index")



