from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = "HomePage"),
    path("gallery", Gallery, name = "Gallery"),
    path("contact", ContactMe, name = "ContactMe"),
    path("error", ErrorPage, name = "ErrorPage"),
    path("newsletter", Newsletter, name = "Newsletter"),
    path("unsubscribe/<str:email>", Unsubscribe, name = "Unsubscribe"),
]

