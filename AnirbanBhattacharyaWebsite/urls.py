from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = "HomePage"),
    path("gallery-view/<str:galug>", Gallery, name = "Gallery"),
    path("contact", ContactMe, name = "ContactMe"),
    path("error", ErrorPage, name = "ErrorPage"),
    path("gallery-verification", GalVeri, name = "GalVeri"),
    path("gallery-va", GalVa, name = "GalVa"),
    path("gallery", Gal, name = "Gal")
]

