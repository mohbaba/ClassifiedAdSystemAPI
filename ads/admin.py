from django.contrib import admin

from ads.models import Ad


# Register your models here.

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'uploader', 'price', 'status', 'category', 'date_posted']
    search_fields = ['title', 'description', 'category', 'uploader', 'price', 'status', 'category', 'date_posted']

