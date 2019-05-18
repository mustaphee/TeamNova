from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)
    phone_no = models.CharField(_("phone_no"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    address = models.CharField(_("address"), max_length=255)
    occupation = models.CharField(_("occupation"), max_length=255)
    dob = models.DateField()