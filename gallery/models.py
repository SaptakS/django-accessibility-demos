from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    attribution = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True)


class SocialIcon(models.Model):
    icon = models.ForeignKey(Image, on_delete=models.CASCADE)
    link = models.URLField(max_length=50)
