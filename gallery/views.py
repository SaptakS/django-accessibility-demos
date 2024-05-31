from django.shortcuts import render

from .models import Image, Article, SocialIcon


def show_images(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(
        request,
        'gallery_article.html',
        {
            'title': article.title,
            'body': article.body,
            'photo': article.photo,
        }
    )

def article_with_icon(request, article_id):
    article = Article.objects.get(pk=article_id)
    icons = SocialIcon.objects.prefetch_related('icon')
    return render(
        request,
        'article_with_social.html',
        {
            'title': article.title,
            'body': article.body,
            'photo': article.photo,
            'icons': icons,
        }
    )
