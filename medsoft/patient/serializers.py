from rest_framework.serializers import ModelSerializer
from .models import Patient, DoctorRequest, MedicalRecord

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorRequestSerializer(ModelSerializer):
    # patient = PatientSerializer(read_only=True)
    class Meta:
        model = DoctorRequest
        fields = '__all__'


class MedicalRecordSerializer(ModelSerializer):
    # patient = PatientSerializer(read_only=True)
    class Meta:
        model = MedicalRecord
        fields = '__all__'
