from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from news.views import NewsListView, NewsDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NewsListView.as_view()),
    path('', NewsDetailView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

