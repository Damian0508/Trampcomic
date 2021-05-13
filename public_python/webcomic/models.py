import os
from django.db import models
from django.dispatch import receiver

# Create your models here.

class Episode(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    counted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to ='webcomic/comic_pages/', null=False, blank=False)

    list_display = ('name', 'episode',)

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Page)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem
    when corresponding `Page` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=Page)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem
    when corresponding `Page` object is updated
    with new file.
    """
    if not instance.pk:
        return False
    
    try:
        old_image = Page.objects.get(pk=instance.pk).image
    except Page.DoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)