from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import random

def otpGen():
    otp = ""
    for i in range(4):
        otp += str(random.randint(1, 9))
    return otp

# Backend of Anirban Bhattacharya Portfolio website by AniWeb.
def index(request):
    return render(request, "index.html")

def Blogs(request):
    return render(request, "blogs.html")

def Gallery(request):
    return render(request, "gallery.html")

def ErrorPage(request):
    return render(request, "error occured.html")

def ContactMe(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        creatingMessage = Contact(Name = name, Email = email, Subject = subject, Message = message)
        creatingMessage.save()
        messages.success(request, "Thank you for contacting me. I will surely try to reply to you as soon as possible.")
        return redirect("HomePage")
    return redirect("ErrorPage")

def Registration(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        creatingUser = User.objects.create_user(email, name, pass1)
        creatingUser.first_name = otpGen()
        creatingUser.last_name = phone
        creatingUser.save()
        messages.success(request, "Thank you for registering.")
        return redirect("HomePage")
    return redirect("ErrorPage")

def Login(request):
    pass

def ForgotPassword(request):
    pass
