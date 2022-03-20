from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from articles.views import createArticle, deleteArticle, getArticle, searchArticles

urlpatterns = [
    path('newArticle',createArticle),
    path('article',deleteArticle),
    path('getArticle',getArticle),
    path('search',searchArticles)
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
