from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from doctor.models import Speciality, Doctor

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(_("address"), max_length=255)
    occupation = models.CharField(_("occupation"), max_length=255)
    dob = models.DateField()

class DoctorRequest(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    message = models.CharField(max_length=500)

class MedicalRecord(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)