from rest_framework import viewsets
from rest_framework.response import Response
from Managment_System.models import Hospital,Doctor
from Managment_System.serializers import HospitalSerializer, DoctorSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
'''
    def list(self, request):
        queryset = self.get_queryset()
        serializer = HospitalSerializer(queryset, many=True)
        data = serializer.data
        for x in data:
            x['pin_code'] = "415211"
        return Response(data)
'''

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer