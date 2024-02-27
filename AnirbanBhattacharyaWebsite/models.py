from django.db import models
from django.contrib.auth.models import User
# Database models of Anirban Bhattacharya.
class Contact(models.Model):
    Name = models.CharField(max_length=40, blank=False, default="")
    Email = models.EmailField(default="", blank=False, max_length=200)
    Subject = models.CharField(default="", max_length=50, blank=False)
    Message = models.TextField(max_length=10000, blank=False, default="")

    def __str__(self):
        return self.Message

class FeaturedBlog(models.Model):
    cat = (
        ("Top Trends", "Top Trends"),
        ("Stock Market", "Stock Market"),
        ("Shark Tank India", "Shark Tank India"),
        ("Technology", "Technology"),
        ("Good Reads", "Good Reads"),
        ("Python", "Python"),
        ("Business News", "Business News"),
    )
    Name = models.CharField(max_length=200, default="")
    Description = models.CharField(max_length=150, default="")
    Keywords = models.CharField(max_length = 2000, default = "")
    DateAdded = models.CharField(max_length=20, default="")
    Image = models.CharField(max_length=300, default="")
    Slug = models.CharField(max_length=300, default="")
    Category = models.CharField(max_length=60, choices=cat)
    Post = models.TextField(max_length=100000, default="")
    Author = models.CharField(max_length=90, default="")
    Views = models.CharField(max_length=400, default="0")
    Likes = models.CharField(max_length=10, default="0")

    def __str__(self):
        return self.Name

class NewsMail(models.Model):
    Email = models.CharField(max_length=60, default="", blank=False)

    def __str__(self):
        return self.Email

class Photo(models.Model):
    Name = models.CharField(max_length = 100, default = "")
    Image = models.ImageField(upload_to="PersonalPhotos")

    def __str__(self):
        return self.Name