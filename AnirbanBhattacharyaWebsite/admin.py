from django.contrib import admin
from .models import *

# Models Registration.
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(IP)
admin.site.register(NewsMail)