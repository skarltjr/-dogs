from rest_framework import serializers
from accounts.serializer import AccountSerializer
from requestArticle.models import RequestArticle

class RequestArticleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()
    requestImage = serializers.ImageField()    
    writer = AccountSerializer()
    class Meta:
        model = RequestArticle
        fields = ('id', 'title', 'content', 'requestImage', 'writer')

