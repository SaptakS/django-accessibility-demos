from django.urls import path

from . import views


urlpatterns = [
    path("", views.show_images, name="show_image"),
    path("article/<int:article_id>/", views.article, name="article"),
    path("article-with-social/<int:article_id>/", views.article_with_icon, name="article_with_icon"),
]
