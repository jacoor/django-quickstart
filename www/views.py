from django.shortcuts import render
from .models import Hero, Footer


def index(request):
    context = {"heroes": Hero.objects.all(), "footer": Footer.objects.first()}
    return render(request, "www/index.html", context)
