from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .serializers import UserSerializer
from rest_framework import permissions

# Create your models here.
# from django.contrib.auth.models import User
from .models import CustomUser


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]