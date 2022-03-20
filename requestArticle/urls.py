from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from requestArticle.views import createRequestArticle, deleteRequestArticle, getRequestArticle, searchRequestArticles


urlpatterns = [
    path('newRequestArticle',createRequestArticle),
    path('getRequestArticle',getRequestArticle),
    path('search',searchRequestArticles),
    path('',deleteRequestArticle)
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
