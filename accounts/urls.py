from django.urls import path,include
from accounts.views import *
import accounts
urlpatterns = [
    path('signUp',SignUp)
]
