from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(
                        max_length=13,
                        unique=False,
                        blank=True)
    otp = models.CharField(
                        max_length=6, 
                        blank=True, 
                        null=True)
    otp_expiry = models.DateTimeField(
                        blank=True,
                        null=True)

    def __str__(self):
        return self.username

