from django.shortcuts import render
from django.views.generic import DetailView

from .models import Hero, Footer, Product


def index(request):
    context = {
        "heroes": Hero.objects.all(),
        "footer": Footer.objects.first(),
        "newest_products": Product.get_newest_products(),
        "featured_products": Product.featured_objects.all()[:6],
        "top_products": Product.top_objects.all()[:9],
    }
    return render(request, "www/index.html", context)


class ProductView(DetailView):
    model = Product
    template_name = "www/product.html"
