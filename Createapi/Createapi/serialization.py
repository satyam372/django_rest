from rest_framework import serializers
from Createapi.models import Login

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields='__all__'