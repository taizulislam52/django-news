from django.contrib import admin
from .models import Post, Tag, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    save_as = True
  

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass