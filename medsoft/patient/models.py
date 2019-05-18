from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(_("address"), max_length=255)
    occupation = models.CharField(_("occupation"), max_length=255)
    dob = models.DateField()