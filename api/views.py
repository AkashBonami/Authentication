from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

class CRUD(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class CRUD1(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUser]

