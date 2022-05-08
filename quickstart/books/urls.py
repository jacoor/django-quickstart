from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("books/", views.BooksListView.as_view(), name="books"),
]