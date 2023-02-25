from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(null=True, unique=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("news-category", kwargs={"slug": self.slug})

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True, unique=True)
    content = models.TextField()
    features_image = models.ImageField(upload_to='static/src/images', blank=True, default='static/src/images/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("news-single", kwargs={"slug": self.slug})

    @property
    def get_features_image_url(self):
        if self.features_image and hasattr(self.features_image, 'url'):
            return self.features_image.url
        else:
            return '/static/src/images/default.png'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    