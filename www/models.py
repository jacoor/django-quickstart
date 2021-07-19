from django.db import models

# Create your models here.
from pathlib import Path
import os


class DatedContent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TitledContent(models.Model):
    title = models.CharField(max_length=50, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Footer(DatedContent, TitledContent):
    content = models.CharField(max_length=255, blank=False)


class Article(DatedContent, TitledContent):
    content = models.TextField()


class Hero(DatedContent, TitledContent):
    image = models.ImageField(upload_to="www/media/hero")


# products


class ProductCategory(DatedContent):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product categories"


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(is_active=False)


class Product(DatedContent):
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#slugfield
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField(help_text="used in urls")
    is_active = models.BooleanField(default=True, help_text="allows to hide product")
    name = models.CharField(max_length=255, blank=False)
    short_description = models.CharField(max_length=255, blank=True)
    descripion = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)

    active_objects = ActiveManager()

    def __str__(self):
        return self.name
