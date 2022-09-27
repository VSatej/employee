from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CATEGORY = (
    (0, 'Active'),
    (1, 'Inactive'),
)

BLOOD_CATEGORY = (
    (0, 'B+'),
    (1, 'O'),
)

MARTIAL_CATEGORY = (
    (0, 'Married'),
    (1, 'Single'),
)

class Employee(AbstractUser):
    name = models.CharField(max_length=100 ,blank=True)
    middle_name = models.CharField(max_length=100 ,blank=True)
    phone_no = models.CharField(max_length=12 ,blank=True)
    alternate_phone_no = models.CharField(max_length=12 ,blank=True)
    dob = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CATEGORY, default=0)
    blood = models.IntegerField(choices=BLOOD_CATEGORY, default=0)
    martial_status = models.IntegerField(choices=MARTIAL_CATEGORY, default=0)

    def __str__(self):
        return self.name