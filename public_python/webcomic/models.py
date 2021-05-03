import os
from django.db import models

# Create your models here.

class Episode(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Page(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to ='webcomic/comic_pages/', null=False, blank=False)

    def __str__(self):
        return os.path.basename(self.image.name)