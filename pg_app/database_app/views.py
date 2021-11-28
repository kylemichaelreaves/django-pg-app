from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PropertySerializer
from .models import Property

# Create your views here.
class PropertyView(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
