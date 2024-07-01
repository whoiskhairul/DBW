from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import NewUser
from .serializers import NewUserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import NewUserSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = NewUserSerializer(user)
        return Response(serializer.data)


class UserUpdateView(generics.UpdateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class UserDeleteView(generics.DestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user