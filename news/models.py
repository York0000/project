from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

