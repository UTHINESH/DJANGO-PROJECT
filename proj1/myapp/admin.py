from django.contrib import admin

# Register your models here.
from .models import Products,User


admin.site.register(Products)
admin.site.register(User)
# admin.site.register(Profile)

