from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def index(request):
    if (request.method == 'GET'):
        return Response({"key": "value"})
    elif (request.method == 'POST'):
        data = request.data
        print(f'****\n{data}\n****')
        return Response({"method": "post"})
    
@api_view(['GET', 'POST'])
def people(request):
    if request.method == 'GET':
        objs = models.Person.objects.all()
        serializer = serializers.PeopleSerializer(
            objs,
            many=True
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = serializers.PeopleSerializer(data= data)

        if (serializer.is_valid()):
            serializer.save()
            print("serializer validation successful!")
            return Response({"message": "person saved successfully!"})
        print("serializer validation was NOT successful!")
        return Response({"error": serializer.errors})