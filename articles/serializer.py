from rest_framework import serializers
from accounts.serializer import AccountSerializer
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()
    reportImage = serializers.ImageField()    
    writer = AccountSerializer()
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'reportImage', 'writer')