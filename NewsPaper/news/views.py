from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['time_creat'] = dateCreation.datetime.date()
        return context


class ArticleList(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'