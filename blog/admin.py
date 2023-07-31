from django.contrib import admin
from .models import Blog


class AdminView(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'date',
    ]


admin.site.register(Blog, AdminView)
