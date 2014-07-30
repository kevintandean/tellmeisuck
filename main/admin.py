from django.contrib import admin

# Register your models here.
from main.models import Post, UserProfile

admin.site.register(Post)
admin.site.register(UserProfile)