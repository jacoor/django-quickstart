from django.contrib import admin

# Register your models here.
from .models import Footer, Article, Hero, ProductCategory, Product


class DateHierarchy(admin.ModelAdmin):
    date_hierarchy = "created"


class ArticleAdmin(DateHierarchy):
    pass


class FooterAdmin(DateHierarchy):
    pass


class HeroAdmin(DateHierarchy):
    pass


# products


class ProductCategoryAdmin(DateHierarchy):
    pass


class ProductAdmin(DateHierarchy):
    # handling slug: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields
    prepopulated_fields = {"slug": ("name",)}
    search_fields = [
        "name",
    ]
    list_filter = ["category", "is_featured", "is_top", "is_active"]
    list_display = ["name", "price", "is_active"] + list_filter


# /products


admin.site.register(Article, ArticleAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(Hero, HeroAdmin)

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
