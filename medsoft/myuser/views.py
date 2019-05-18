from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework import status, response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
import requests

# Create your views here.

class UserProfileViewSet(GenericViewSet, mixins.ListModelMixin):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        return Response(UserSerializer(request.user).data)