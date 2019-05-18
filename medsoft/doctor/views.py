from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, response
from rest_framework.decorators import action
from .models import Doctor
from .serializers import DoctorSerializer
import requests

# Create your views here.

class DoctorViewSet(ModelViewSet):
    model = Doctor
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer