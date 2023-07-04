from django.db import models
from django.core.validators import RegexValidator
from loginapp.models import User

#CUSTOMER

class Customer(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    name = models.CharField(max_length=100, blank=False, null=False)
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    mobile_number = models.CharField(validators=[mobile_regex], max_length=14, blank=True)
    gender = models.CharField(max_length=6, blank=False, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

#CUSTOMER

