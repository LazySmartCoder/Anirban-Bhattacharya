from django.db import models
from django.contrib.auth.models import User
# Database models of Anirban Bhattacharya.
class Contact(models.Model):
    Name = models.CharField(max_length=40, blank=False, default="")
    Email = models.EmailField(default="", blank=False, max_length=200)
    Subject = models.CharField(default="", max_length=50, blank=False)
    Message = models.TextField(max_length=1000, blank=False, default="")

    def __str__(self) -> str:
        return self.Message

class Blog(models.Model):
    cat = (
        ("Coding", "Coding"),
        ("Python", "Python"),
        ("Business", "Business"),
        ("Stock Market", "Stock Market"),
    )
    Name = models.CharField(max_length=200, default="")
    Description = models.CharField(max_length=150, default="")
    DateAdded = models.CharField(max_length=20, default="")
    Image = models.CharField(max_length=300, default="")
    Slug = models.CharField(max_length=300, default="")
    Category = models.CharField(max_length=60, choices=cat)
    Post = models.TextField(max_length=100000, default="")
    Author = models.CharField(max_length=90, default="")
    Views = models.CharField(max_length=400, default="0")
    Likes = models.CharField(max_length=10, default="0")

    def __str__(self) -> str:
        return self.Name

class IP(models.Model):
    IP = models.CharField(max_length=50, default="")
    BlogSlug = models.CharField(max_length=100, default="")
    
    def __str__(self) -> str:
        return self.IP


