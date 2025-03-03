# created manually!
from . import models
from rest_framework import serializers

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Person
        fields = [
            'id',
            'name',
            'age'
        ]