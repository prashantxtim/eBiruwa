from django.shortcuts import render,redirect
# from donor.forms import CustomerForm
# from donor.models import Donor

# Create your views here.
# def donorform(request):
#     if request.method=="POST":

#         customers=CustomerForm(request.POST,request.FILES)

#         if customers.is_valid():

#             try:

#                 customers.save()
#                 return redirect ("/home")

#             except:

#                 print("INVALID")
#     else:

#         customers=CustomerForm()
#     return render (request,"LoginRegister.html",{'customers':customers})

# def signin(request):
#     if request.method=='POST':
#         donor_name=request.post.get('donor_username')
#         donor_password=request.post.get('donor_password')
#         user=Donor.objeects.get(donor_username=donor_name,donor_password=donor_password)
#         if user is not None:
#             return redirect("/index")

#     return render (request,"LoginRegister.html")

# def index(request):
#     return render(request,"index.html")



