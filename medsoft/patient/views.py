from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, response
from rest_framework.decorators import action
from .models import Patient
from .serializers import PatientSerializer
import requests

# Create your views here.

class PatientViewSet(ModelViewSet):
    model = Patient
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer