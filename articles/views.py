from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from accounts.models import Account
from articles.serializer import ArticleSerializer
import json
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.


@api_view(['POST'])
def createArticle(request):
    data = request.POST
    image = request.FILES['reportImage']
    if not Account.objects.filter(id=data['writerId']).exists():
        raise Account.DoesNotExist()
    else :
        user= Account.objects.filter(id=data['writerId']).get()

    article = Article.objects.create(
        title = data['title'],
        content = data['content'],
        reportImage = image,
        writer = user
    )
    article.save()
    if article:
        return JsonResponse({'message':'success to create article'},status=200)
    else:
        return JsonResponse({'message':'fail to create article'},status=400)

@api_view(['GET'])
def getArticle(request):
    data = json.loads(request.body)
    targetId = data['articleId']
    article = Article.objects.filter(id=targetId).get()
    return JsonResponse({'article': ArticleSerializer(article).data},status=200)

@api_view(['GET'])
def searchArticles(request):
    data = json.loads(request.body)
    keyword = data['keyword']
    article = Article.objects.all().filter(Q(title__contains=keyword))
    if article:
        article = article.get() # 여러 게시글 리턴하는 방법 알아보기
        return JsonResponse({'articles': ArticleSerializer(article).data},status=200)    
    else:
        return JsonResponse({'message':"검색 조건에 해당하는 글이 없습니다"},status =404)


@api_view(['DELETE'])
def deleteArticle(request):
    data = json.loads(request.body)
    targetId = data['articleId']
    article = Article.objects.filter(id=targetId).delete()

    
    return JsonResponse({'message':'success to delete article'},status=200)