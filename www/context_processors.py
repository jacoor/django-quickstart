from .models import Footer, Article
import math


def custom_context_processor(request):
    footer_articles_count = Article.active_objects.filter(is_in_footer=True).count()
    footer_articles_count_half = math.ceil(footer_articles_count / 2)
    context = {
        "footer": Footer.objects.first(),
        "top_menu_articles": Article.active_objects.filter(is_in_top_menu=True),
        "footer_articles_left": Article.active_objects.filter(is_in_footer=True)[
            :footer_articles_count_half
        ],
        "footer_articles_right": Article.active_objects.filter(is_in_footer=True)[
            footer_articles_count_half:footer_articles_count
        ],
    }
    return context
