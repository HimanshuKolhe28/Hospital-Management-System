
from Managment_System.models import  Hospital
from rest_framework import serializers
from Managment_System.models import Hospital,Doctor

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
        


class DoctorSerializer(serializers.ModelSerializer):
    # hospital = serializers.PrimaryKeyRelatedField(queryset=Hospital.objects.all(), write_only=True)
    # hospital_data =  HospitalSerializer(read_only=True, source='hospital')
    
    class Meta:
        fields = '__all__'
        model = Doctor  