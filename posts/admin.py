from django.contrib import admin

from .models import Tag, Comment, Post

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Post)
