from django.contrib import admin
from .models import Blog

admin.site.register(Blog) #This line for telling admin to put which databse model into database
