from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def invalidlogin(request):
    return render('loggedin.html',{"full_name":request.user.username})

def home(request):
    return render(request,'home.html')