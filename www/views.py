from django.shortcuts import render
from .models import Hero


def index(request):
    context = {"heroes": Hero.objects.all()}
    return render(request, "www/index.html", context)
