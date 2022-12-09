from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView # new


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView): # new
    serializer_class = LoginSerializer
