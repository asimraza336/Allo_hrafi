from django.db import models

from django.contrib.auth.models import AbstractUser
from AdminApp.models import City
# from django.contrib.auth import get_user_model
# User = get_user_model()

USER_ROLES = (
        ('Provider', 'Provider'),
        ('Client', 'Client')
    )

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

class User(AbstractUser):
    
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50,null=True,blank=True,unique=True)
    is_phone_verified = models.BooleanField(default=False, null=True, blank=True)
    otp_code = models.IntegerField(null=True, blank=True)
    user_role = models.CharField(
        max_length=15, choices=USER_ROLES, default="Admin")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(
        upload_to="Profile_Pictures/", null=True, blank=True, default="Profile_Pictures/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username