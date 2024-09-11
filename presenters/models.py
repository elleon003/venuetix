from django.db import models
from django.conf import settings


class Presenter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    