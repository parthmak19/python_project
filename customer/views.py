from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth


# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email_id = request.POST['email-id']
        dob = request.POST['dob']
        phone_no = request.POSt['phone_no']
        username = request.POST['username']
        password = request.POST['password']

        customer = User.objects.create_user(fullname=fullname, email=email_id, dob=dob, phone_no=phone_no,
                                            username=username, password=password)
        customer.save()
        return redirect('/')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        customer = auth.authenticate(username=user, password=password)

        if customer is not None:
            auth.login(request, customer)
            return redirect('/')
        else:
            messages.warning(request, "Invalid Username and Password!")
            return redirect('login.html')

    else:
        return render(request, 'login.html')


def viewDashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
