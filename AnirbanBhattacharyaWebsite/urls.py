from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = "HomePage"),
    path("blogs", Blogs, name = "Blogs"),
    path("gallery", Gallery, name = "Gallery"),
    path("contact", ContactMe, name = "ContactMe"),
    path("error", ErrorPage, name = "ErrorPage"),
    path("register", Registration, name = "Registration"),
    path("login", Login, name = "Login"),
    path("forgot-password", ForgotPassword, name = "ForgotPassword"),
]

