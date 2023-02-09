from django.contrib import admin
from .models import Post, Tag, Category


# Register your models here.
@admin.register(Post, Category, Tag)


class CategoryAdmin(admin.ModelAdmin):
    pass