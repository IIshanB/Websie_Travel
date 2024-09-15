from django.contrib.auth.models import User
from django.db import models
import random


# Create your models here.

class TimeStamp(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save()

    def is_valid(self):
        # OTP is valid for 5 minutes
        from datetime import timedelta
        return self.created_at >= timezone.now() - timedelta(minutes=5)