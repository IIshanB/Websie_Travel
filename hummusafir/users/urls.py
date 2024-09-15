# users/urls.py
from django.urls import path
from .views import UserRegistrationView, OTPVerificationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('verify-otp/', OTPVerificationView.as_view(), name='verify-otp'),
]
