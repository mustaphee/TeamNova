from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer as RestAuthRegisterSerializer
from allauth.account import app_settings as allauth_settings
from patient.serializers import PatientSerializer
from doctor.serializers import DoctorSerializer
from django.contrib.auth.models import User

PATIENT_USER = 'P'
DOCTOR_USER = 'D'

class RegisterSerializer(RestAuthRegisterSerializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    username = serializers.CharField(required=True)
    user_type = serializers.CharField(max_length=2, required=True, help_text="Type of user \n P - patient, D - doctor")
    # doctor = DoctorSerializer(required=False)
    # patient = PatientSerializer(required=False)

    address = serializers.CharField(required=True, max_length=255)
    occupation = serializers.CharField(required=True, max_length=255)
    dob = serializers.DateField(required=True)

    hospital = serializers.CharField(required=False, max_length=50)
    speciality = serializers.IntegerField(required=False)

    def validate_hospital(self, value):
        data = self.initial_data.get('user_type', '')
        if data == DOCTOR_USER and not value:
            raise serializers.ValidationError("hospital field is required for user of type 'D'")

    def validate_speciality(self, value):
        data = self.initial_data.get('douser_typector', '')
        if data == DOCTOR_USER and not value:
            raise serializers.ValidationError("speciality field is required for user of type 'D'")

    def validate_patient(self, value):
        patient = PatientSerializer(data=value)
        patient.is_valid(raise_exception=True)
        return value

    def validate_user_type(self, value):
        """
        Check that the blog post is about Django.
        """
        if value not in [DOCTOR_USER, PATIENT_USER]:
            raise serializers.ValidationError("serType must be one of 'P' or 'E'")
        return value

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'username': self.validated_data.get('username', ''),
            'address': self.validated_data.get('address', ''),
            'occupation': self.validated_data.get('occupation', ''),
            'dob': self.validated_data.get('dob', ''),

            'hospital': self.initial_data.get('hospital', ''),
            'speciality': self.initial_data.get('speciality', ''),
        }

    def custom_signup(self, request, user):
        user_type = self.validated_data.get('user_type', '')
        serializer = None
        if user_type == DOCTOR_USER:
            data = self.get_cleaned_data()
            data['user'] = user.id
            serializer = DoctorSerializer(data=data)
        else:
            data = self.get_cleaned_data()
            data['user'] = user.id
            serializer = PatientSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

class UserSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()
    user_type = serializers.SerializerMethodField()
    phone_no = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('phone_no', 'username', 'name', 'email', 'doctor', 'patient', 'user_type')

    def get_user_type(self, obj):
        try:
            patient = obj.patient
            return PATIENT_USER
        except:
            return DOCTOR_USER

    def get_phone_no(self, obj):
        return obj.username

    def get_name(self, obj):
        return obj.first_name + obj.last_name