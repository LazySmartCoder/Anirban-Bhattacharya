from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import random

# Backend of Anirban Bhattacharya Portfolio website.

def sendEmail(email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = formataddr((str(Header('Anirban Bhattacharya')), "no-reply@anirbanbhattacharya.in"))
    msg['To'] = email
    msg["Subject"] = subject
    html = message
    msg.attach(MIMEText(html, 'html'))
    s = smtplib.SMTP('smtp.gmail.com', port=587)
    s.starttls()
    s.login("contact.anirbanbhattacharya@gmail.com", "esrdrljzrkdmfhzb")
    s.sendmail("no-reply@anirbanbhattacharya.in", email, msg.as_string())
    s.quit()
    return None

def galotp():
    string = ""
    for i in range(4):
        string += str(random.randint(0, 9))
    return string

def index(request):
    return render(request, "index.html", {"blogs" : FeaturedBlog.objects.all()})

def Gallery(request, galug):
    photo = Photo.objects.all()
    if GalVerifi.objects.filter(OTP = galug).exists():
        otp = GalVerifi.objects.get(OTP = galug)
        otp.delete()
        return render(request, "gallery.html", {"photo" : photo})
    else:
        return redirect("GalVeri")

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
        sendEmail("contact.anirbanbhattacharya@gmail.com", "Someone contacted you!", f"Name: {name}, Email: {email}, Message: {message}")
        return redirect("HomePage")
    return redirect("ErrorPage")

def GalVeri(request):
    return render(request, "galveri.html")

def Gal(request):
    return redirect("GalVeri")

def GalVa(request):
    name = request.POST["name"]
    email = request.POST["email"]
    au = request.POST["au"]
    createOtp = GalVerifi(OTP = galotp())
    createOtp.save()
    sendEmail("contact@anirbanbhattacharya.in", "Gallery OTP", f"Hey, someone has requested access to your website gallery. Email ID of anonymous - {email}, Name - {name}, Description - {au}, Access Link - https://anirbanbhattacharya.in/gallery-view/{GalVerifi.objects.last().OTP}")
    messages.success(request, "Gallery Access Requested!")
    return redirect("/")
