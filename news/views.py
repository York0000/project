from django.views.generic import ListView, DetailView

from news.models import NewsModel


class NewsListView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return NewsModel.objects.order_by('-pk')[:8]


class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    model = NewsModel
