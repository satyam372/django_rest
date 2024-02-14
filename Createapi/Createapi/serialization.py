# Assuming SerializationClass is defined in serializers.py
from rest_framework import serializers
from .models import Login

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['name', 'passs']