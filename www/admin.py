from django.contrib import admin

# Register your models here.
from .models import Footer, Article, Hero


class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = "created"


class FooterAdmin(admin.ModelAdmin):
    date_hierarchy = "created"


class HeroAdmin(admin.ModelAdmin):
    date_hierarchy = "created"


admin.site.register(Article, ArticleAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(Hero, HeroAdmin)
