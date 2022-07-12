from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = "HomePage"),
    path("blogs", Blogs, name = "Blogs"),
    path("gallery", Gallery, name = "Gallery"),
    path("contact", ContactMe, name = "ContactMe"),
    path("error", ErrorPage, name = "ErrorPage"),
]

