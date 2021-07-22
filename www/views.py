from django.shortcuts import render
from .models import Hero, Footer, Product


def index(request):
    context = {
        "heroes": Hero.objects.all(),
        "footer": Footer.objects.first(),
        "newest_products": Product.get_newest_products(),
    }
    return render(request, "www/index.html", context)
