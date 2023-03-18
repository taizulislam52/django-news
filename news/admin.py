from django.contrib import admin
from .models import Post, Tag, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "color")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",'category','section')
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["tags", 'category', 'author']
    search_fields = ["title", "content", 'section']
    save_as = True
  

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]