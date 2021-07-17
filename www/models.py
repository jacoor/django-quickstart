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
