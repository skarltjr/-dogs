from rest_framework.response import Response
from rest_framework.decorators import api_view
from requestArticle.models import RequestArticle
from accounts.models import Account
from requestArticle.serializer import RequestArticle, RequestArticleSerializer
import json
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.


@api_view(['POST'])
def createRequestArticle(request):
    data = request.POST
    image = request.FILES['requestImage']
    if not Account.objects.filter(id=data['writerId']).exists():
        raise Account.DoesNotExist()
    else :
        user= Account.objects.filter(id=data['writerId']).get()

    requestArticle = RequestArticle.objects.create(
        title = data['title'],
        content = data['content'],
        requestImage = image,
        writer = user
    )
    requestArticle.save()
    if requestArticle:
        return JsonResponse({'message':'success to create requestArticle'},status=200)
    else:
        return JsonResponse({'message':'fail to create requestArticle'},status=400)

@api_view(['GET'])
def getRequestArticle(request):
    data = json.loads(request.body)
    targetId = data['requestArticleId']
    requestArticle = RequestArticle.objects.filter(id=targetId).get()
    return JsonResponse({'article': RequestArticleSerializer(requestArticle).data},status=200)

@api_view(['GET'])
def searchRequestArticles(request):
    data = json.loads(request.body)
    keyword = data['keyword']
    requestArticle = RequestArticle.objects.all().filter(Q(title__contains=keyword))
    if requestArticle:
        requestArticle = requestArticle.get() # 여러 게시글 리턴하는 방법 알아보기
        return JsonResponse({'requestArticles': RequestArticleSerializer(requestArticle).data},status=200)    
    else:
        return JsonResponse({'message':"검색 조건에 해당하는 글이 없습니다"},status =404)

@api_view(['DELETE'])
def deleteRequestArticle(request):
    data = json.loads(request.body)
    targetId = data['requestArticleId']
    requestArticle = RequestArticle.objects.filter(id=targetId).delete()

    
    return JsonResponse({'message':'success to delete requestArticle'},status=200)