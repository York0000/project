from django.contrib import admin

from news.models import NewsModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'created_at']
    list_filter = ['created_at']



