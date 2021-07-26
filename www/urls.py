from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/<int:pk>/<slug:slug>", views.ProductView.as_view(), name="product"),
]
