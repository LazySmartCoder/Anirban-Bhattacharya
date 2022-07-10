from django.shortcuts import render

# Backend of Anirban Bhattacharya Portfolio website by AniWeb.
def index(request):
    return render(request, "index.html")

def Blogs(request):
    return render(request, "blogs.html")

def Gallery(request):
    return render(request, "gallery.html")