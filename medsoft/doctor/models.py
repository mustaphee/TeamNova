from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.
class Speciality(models.Model):
    title = models.CharField(max_length=30)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.CharField(_("hospital"), max_length=50)
    address = models.CharField(_("address"), max_length=255)
    dob = models.DateField()
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)