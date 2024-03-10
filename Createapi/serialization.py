from rest_framework import serializers
from .models import Login, Raisecomplaint, Raisecomplaint_2

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['name', 'passs']

class RaiseissueSerializer(serializers.ModelSerializer):  # Corrected line
    class Meta:
        model = Raisecomplaint
        fields = '__all__'

class Raiseissue_2Serializer(serializers.ModelSerializer):  # Corrected line
    photo_of_issue = serializers.ImageField(required=False)
    # explanation of above statement
    # This assignment implies that when serializing a Raisecomplaint_2 instance, 
    # the complaint field should be serialized using the RaisecomplaintSerializer. 
    # This results in a nested representation of the related Raisecomplaint instance 
    # within the serialized output of a Raisecomplaint_2 instance.
    
    class Meta:
        model = Raisecomplaint_2
        fields = '__all__'



from rest_framework import serializers

class CombinedComplaintsSerializer(serializers.Serializer):
    complaint_id = serializers.IntegerField()
    emp_id = serializers.IntegerField(required=False)
    department = serializers.CharField(required=False)
    problem = serializers.CharField(required=False)
    sub_problem = serializers.CharField(required=False)
    engineer = serializers.CharField(required=False)
    descrp = serializers.CharField(required=False)
    priority = serializers.CharField(required=False)
    photo_of_issue = serializers.ImageField(required=False)
    floor = serializers.CharField(required=False)
