from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    attribution = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(
        help_text="Used in alt attribute to describe image.",
    )

    def __str__(self):
        return self.title


class Article(models.Model):
    LANG = [
        ("en", "English"),
        ("es", "Español"),
    ]
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True)
    photo_description = models.TextField(
        blank=True, null=True,
        help_text="Used in alt attribute to describe image in context of the article."
    )
    is_decorative = models.BooleanField(
        default=False,
        help_text="Is the image decorative in this context?",
    )
    language = models.CharField(max_length=2, choices=LANG, default="en")


class SocialIcon(models.Model):
    icon = models.ForeignKey(Image, on_delete=models.CASCADE)
    link = models.URLField(max_length=50)
    linktext = models.CharField(
        max_length=100,
        help_text="Name of the social media."
    )
