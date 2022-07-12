from django.db import models

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
    Name = models.CharField(max_length=20, default="")
    Description = models.CharField(max_length=200, default="")
    DateAdded = models.CharField(max_length=20, default="")
    Image = models.CharField(max_length=300, default="")
    Slug = models.CharField(max_length=300, default="")
    Category = models.CharField(max_length=60, choices=cat)
    Post = models.TextField(max_length=10000, default="")
    Author = models.CharField(max_length=90, default="")
    Views = models.CharField(max_length=400, default="")
    Likes = models.CharField(max_length=400, default="")



