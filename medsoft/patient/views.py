from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, response, mixins, viewsets, exceptions
from rest_framework.decorators import action
from .models import Patient, DoctorRequest, MedicalRecord
from .serializers import PatientSerializer, DoctorRequestSerializer, MedicalRecordSerializer
import requests

# Create your views here.

class PatientViewSet(ModelViewSet):
    model = Patient
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorRequestViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    model = DoctorRequest
    queryset = DoctorRequest.objects.all()
    serializer_class = DoctorRequestSerializer

    def get_queryset(self):
        return self.queryset

    @action(detail=False, methods=['POST'])
    def create_request(self, request):
        try:
            user = request.user.patient
        except:
            raise exceptions.PermissionDenied("Only a patient can access this route")
        data = request.data.copy()
        data['patient'] = request.user.patient.id
        serializer = DoctorRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def accepted_requests(self, request):
        is_doctor = False
        try:
            user = self.request.user.doctor
            is_doctor = True
        except:
            raise exceptions.PermissionDenied("Only a doctor can access this route")
        return response.Response(DoctorRequestSerializer(DoctorRequest.objects.filter(doctor=self.request.user.doctor), many=True).data)
    @action(detail=True, methods=['POST'])
    def accept(self, request, *args, **kwargs):
        """
            Create a doctor request
        """
        try:
            user = request.user.doctor
        except:
            raise exceptions.PermissionDenied("Only a doctor can access this route")
        obj = self.get_object()
        if obj.accepted:
            raise exceptions.ValidationError("Doctor request has been accepted")
        else:
            obj.doctor = request.user.doctor
            obj.accepted = True
            obj.save()
        return response.Response(DoctorRequestSerializer(obj).data)


class MedicalRecordViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    model = MedicalRecord
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        is_doctor = False
        try:
            user = self.request.user.doctor
            is_doctor = True
        except:
            raise exceptions.PermissionDenied("Only a doctor can access this route")
        if not is_doctor:
            return MedicalRecord.objects.filter(patient=self.request.patient)
        return MedicalRecord.objects.filter(doctor=self.request.doctor)

    @action(detail=False, methods=['POST'])
    def create_request(self, request):
        try:
            user = request.user.doctor
        except:
            raise exceptions.PermissionDenied("Only a doctor can access this route")
        data = request.data.copy()
        data['doctor'] = request.user.patient.id
        serializer = MedicalRecordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)