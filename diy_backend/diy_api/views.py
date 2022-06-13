from django.shortcuts import render
from rest_framework import generics
from .serializers import GuideSerializer
from .models import Guide

# Create your views here.
class GuideList(generics.ListCreateAPIView):
    queryset = Guide.objects.all().order_by('id')
    serializer_class = GuideSerializer

class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all().order_by('id')
    serializer_class = GuideSerializer