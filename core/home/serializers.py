# created manually!
from . import models
from rest_framework import serializers


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer() # it will only show color_name field based on the ColorSerializer
    color_info = serializers.SerializerMethodField()
    class Meta:
        model = models.Person
        # fields = [
        #     'id',
        #     'name',
        #     'age',
        #     'created_on'
        # ]
        fields = '__all__'
        # depth = 1 # for populating foreign key, value can be high if more fields are required
        
    def get_color_info(self, obj):
        # color_obj = models.Color.objects.get(id = obj.color.id)
        # return {
        #     'color_name': color_obj.color_name,
        #     'hex_code': '#000'
        # }
        if obj.color != None:
            return {
                'color_info_name': models.Color.objects.get(id = obj.color.id).color_name,
                'hex_code': '#000'
            }
        print(f'color ID found: {obj.color != None }')
        return "Not Found"
        
    def validate_name(self, name):
        special_chars = '''!@#$%^&*()_+-=[]}{:"|;'\\<>?,./<'''
        if any(c in special_chars for c in name):
            raise serializers.ValidationError("Name Must Not contain any special characters!")
        return name
        
    def validate(self, data): # for single field validate_FieldName can be used
        if data["age"] < 18:
            raise serializers.ValidationError("Age Must be >= 18")
        return data # this returns valid data to the serializer