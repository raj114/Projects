from rest_framework import serializers

from .models import AppUsers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        fields= '__all__'

class EncodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncodedData
        fields= '__all__'

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanData
        fields= '__all__'