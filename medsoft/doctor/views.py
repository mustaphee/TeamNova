from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import status, response
from rest_framework.decorators import action
from .models import Doctor, Speciality
from .serializers import DoctorSerializer, SpecialitySerializer
import requests

# Create your views here.

class DoctorViewSet(ModelViewSet):
    model = Doctor
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class SpecialityViewSet(ReadOnlyModelViewSet):
    model = Speciality
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer