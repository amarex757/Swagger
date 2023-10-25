from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from app.serializers import EmissionSerializer
from .models import * 
from .serializers import * 

class GetMethod(viewsets.ModelViewSet):
    queryset = Emissions.objects.all()
    serializer_class = EmissionSerializer

    def list(self, request, *args, **kwargs):
        data = list(Emissions.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Emissions.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        emission_serializer_data = EmissionSerializer(data=request.data)
        if emission_serializer_data.is_valid():
            emission_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Emission Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        emission_data = Emissions.objects.filter(id=kwargs['pk'])
        if emission_data:
            emission_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Emission Deleted Successfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Emission data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        emission_details = Emissions.objects.get(id=kwargs['pk'])
        emission_serializer_data = EmissionSerializer(
            emission_details, data=request.data, partial=True)
        if emission_serializer_data.is_valid():
            emission_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Emission Updated Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Emission data not found", "status": status_code})
