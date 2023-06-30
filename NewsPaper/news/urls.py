from django.urls import path
from .views import NewsList, ArticleList

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', ArticleList.as_view()),
]