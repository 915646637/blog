from django.shortcuts import render
from rest_framework.generics import ListAPIView

# Create your views here.
from main.models import Nav
from main.serializers import NavSerializers


class NavAPIView(ListAPIView):

    serializer_class = NavSerializers
    queryset = Nav.objects.all()

