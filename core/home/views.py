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
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
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
    
    elif request.method == 'PUT': # PATCH supports partial updates to one or more fields but PUT does not support partial updates
        data = request.data
        if "id" not in data.keys():
            return Response({"error": "Invalid Operation! Updation Failed"})
        obj = models.Person.objects.get(id = data['id'])
        if not obj:
            return Response({"error": "Invalid Operation!"})
        serializer = serializers.PeopleSerializer(
            obj,
            data = data
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "person updated successfully!"})
        return Response({"error": serializer.errors})

    elif request.method == 'PATCH':
        data = request.data
        if "id" not in data.keys():
            return Response({"error": "Invalid Operation! Updation Failed"})
        obj = models.Person.objects.get(id = data['id'])
        if not obj:
            return Response({"error": "Invalid Operation!"})
        serializer = serializers.PeopleSerializer(
            obj,
            data = data,
            partial = True # this is important!
        )
        if serializer.is_valid():
            
            serializer.save()
            return Response({"message": "person patched successfully!"})
        return Response({"error": serializer.errors})

    elif request.method == 'DELETE':
        data = request.data
        # print(f'Type of Data: {type(data)}\nKeys in Data: {data.keys()}\nID in keys: {"id" in data.keys()}')
        if "id" not in data.keys():
            return Response({"error": "Invalid Operation! Deletion Failed"})
        obj = models.Person.objects.get(id = data['id'])
        if not obj:
            return Response({"error": "Invalid Operation!"})
        obj.delete()
        return Response({'message': f"Deletion of ID: {data['id']} Successfull!"})



    