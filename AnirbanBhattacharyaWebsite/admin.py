from django.contrib import admin
from .models import *

# Models Registration.
admin.site.register(Contact)
admin.site.register(FeaturedBlog)
admin.site.register(NewsMail)
admin.site.register(Photo)