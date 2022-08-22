from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = "HomePage"),
    path("blogs", Blogs, name = "Blogs"),
    path("gallery", Gallery, name = "Gallery"),
    path("contact", ContactMe, name = "ContactMe"),
    path("error", ErrorPage, name = "ErrorPage"),
    path("read-blog/<str:blogslug>", ReadBlogs, name = "ReadBlogs"),
    path("like-blog/<str:likeblog>", LikeBlog, name = "LikeBlog"),
    path("hire", Hire, name = "Hire"),
    path("hire-me", HireMe, name = "HireMe"),
]

