from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import random
import smtplib
import socket
from requests import get

# Backend of Anirban Bhattacharya Portfolio website by AniWeb.

def sendEmail(name, email, subject, message):
    send = smtplib.SMTP("smtp.gmail.com", port=587)
    send.starttls()
    send.login("anirbanbhattacharya.me@gmail.com", "hsdcbgfuuglkeelt")
    send.sendmail("anirbanbhattacharya.me@gmail.com", email, f"Subject: {subject}\n" + f"Hello {name}\n,{message}")
    send.quit()

def index(request):
    return render(request, "index.html", {"blogs" : Blog.objects.all()})

def Blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html", {"blogs" : blogs})

def Gallery(request):
    return render(request, "gallery.html")

def ErrorPage(request, exception):
    # This is for handler 404
    return render(request, "error page.html")

def ErrorOccured(request):
    # This is for handler 500
    return render(request, "error page.html")

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

def ReadBlogs(request, blogslug):
    blogs = Blog.objects.get(Slug = blogslug)
    blogs.Views = str(int(blogs.Views) + 1)
    blogs.save()
    param = {
        "name" : blogs.Name,
        "author" : blogs.Author,
        "date" : blogs.DateAdded,
        "views" : blogs.Views,
        "image" : blogs.Image,
        "desc" : blogs.Description,
        "post" : blogs.Post, 
        "cat" : blogs.Category,
        "likes" : blogs.Likes,
        "slug" : blogs.Slug,
        "blogs" : Blog.objects.all()
    }
    return render(request, "read blogs.html", param)

def LikeBlog(request, likeblog):
    ip = request.POST["ip"]
    blog = Blog.objects.get(Slug = likeblog)
    if IP.objects.filter(IP = ip, BlogSlug = likeblog).exists():
        messages.warning(request, "You already liked the blog post.")
        return redirect(f"/read-blog/{likeblog}")
    addingIp = IP(IP = str(ip), BlogSlug = likeblog)
    addingIp.save()
    blog.Likes = str(int(blog.Likes) + 1)
    blog.save()
    messages.success(request, "Thank you for liking this blog post.")
    return redirect(f"/read-blog/{likeblog}")

def Hire(request):
    return render(request, "hire.html")

def HireMe(request):
    if request.method == "POST":
        Name = request.POST["name"]
        Email = request.POST["email"]
        Phone = request.POST["phone"]
        Service = request.POST["service"]
        Subject = request.POST["subject"]
        Budget = request.POST["budget"]
        Message = request.POST["message"]
        creatingHired = Hired(Name = Name, Email = Email, Phone = Phone, Service = Service, Subject = Subject, Budget = Budget, Message = Message)
        creatingHired.save()
        messages.success(request, "Thank you for sending me a hiring request. I will contact you via your email or your contact number.")
        return redirect("Hire")
    return redirect("ErrorPage")

