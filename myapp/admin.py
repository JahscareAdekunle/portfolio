from django.contrib import admin
from .models import Message,Post,Comment, Category
# Register your models here.
admin.site.register(Message)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)