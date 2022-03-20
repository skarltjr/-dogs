from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Account
from accounts.serializer import AccountSerializer
import json
from django.http import JsonResponse
# Create your views here.


@api_view(['POST'])
def SignUp(request):
    data = json.loads(request.body)
    user = Account.objects.create(
        email = data['email'],
        password = data['password'],
        name = data['name']
    )
    if user:
        return JsonResponse({'message':'success to signUp'},status=200)
    else:
        return JsonResponse({'message':'fail to signUp'},status=400)