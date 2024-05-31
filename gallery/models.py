from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    attribution = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(
        help_text="Used in alt attribute to describe image."
    )

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True)
    photo_description = models.TextField(
        help_text="Used in alt attribute to describe image in context of the article."
    )


class SocialIcon(models.Model):
    icon = models.ForeignKey(Image, on_delete=models.CASCADE)
    link = models.URLField(max_length=50)
