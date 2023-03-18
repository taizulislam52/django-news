from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.forms.widgets import TextInput
import uuid

class ColorField(models.CharField):
    description = "Field for storing RGB color value"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        super().__init__(*args, **kwargs)
    
    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        kwargs['widget'] = TextInput(attrs={'type': 'color'})
        return super(ColorField, self).formfield(**kwargs)
    
    def db_type(self, connection):
        return 'CharField'
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value

    def get_prep_value(self, value):
        return value
    
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(null=True, unique=True)
    color = ColorField(blank=True)

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
    SECTION = (
        ('Popular', 'Popular'),
        ('Trending', 'Trending'),
        ('Most View', 'Most View'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True, unique=True)
    content = models.TextField()
    features_image = models.ImageField(upload_to='news', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.CharField(choices=SECTION, max_length=200, blank=True)
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
    