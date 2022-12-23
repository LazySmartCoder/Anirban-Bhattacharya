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
    path("newsletter", Newsletter, name = "Newsletter"),
    path("search", SearchBlogs, name = "SearchBlogs"),
    path("autosuggest", AutoSuggest, name = "AutoSuggest"),
    path("unsubscribe/<str:email>", Unsubscribe, name = "Unsubscribe"),
]

