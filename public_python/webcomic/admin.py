from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User, Group
from django.db import models
from django import forms
from .models import Episode, Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': forms.FileInput(attrs={'multiple': True})},
    }

    readonly_fields = ('image_view',)
    # def save_model(self, request, obj, form, change):
        # super(MyAdminView, self).save_model(request, obj, form, change)

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="350" height="450" style="object-fit:contain" />')

admin.site.site_header = 'Tramp webcomic - panel'
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Episode)
admin.site.register(Page, PageAdmin)


