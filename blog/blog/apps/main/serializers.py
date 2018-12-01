from django.contrib.auth import login
from rest_framework import serializers

from main.models import Nav
from passport.models import User


class NavSerializers(serializers.ModelSerializer):

    class Meta:
        model = Nav
        fields = ("id", 'name', 'url')



