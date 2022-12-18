from django.contrib import admin
from .models import Articles

# Register your models here.

class ArtcilesAdmin(admin.ModelAdmin):
    fields = [
            "name",
            "stock",
            "price",
            "image_url"
        ]

admin.site.register(Articles)