from django.shortcuts import render

from rest_framework.decorators import APIView

# Create your views here.
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets


class ProfileView(viewsets.ModelViewSet):


        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer

