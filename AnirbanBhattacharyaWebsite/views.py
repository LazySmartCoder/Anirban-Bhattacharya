from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

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

