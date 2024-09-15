# users/views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import OTP
from .serializers import UserSerializer, OTPVerificationSerializer

class UserRegistrationView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp = OTP.objects.create(user=user)
            otp.generate_otp()
            # Send OTP to user's mobile number (implementation required)
            return Response({'message': 'User registered successfully. OTP sent to your mobile.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OTPVerificationView(APIView):
    def get(self, request):
        return render(request, 'verify_otp.html')

    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            otp_input = serializer.validated_data['otp']
            try:
                user = User.objects.get(username=username)
                otp_record = OTP.objects.filter(user=user).last()
                if otp_record and otp_record.is_valid() and otp_record.otp == otp_input:
                    # OTP is valid, proceed with user activation (or login)
                    user.is_active = True
                    user.save()
                    return Response({'message': 'OTP verified successfully. User is now active.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Invalid or expired OTP.'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
