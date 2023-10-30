from rest_framework import serializers
from .models import Person , Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            'color_name'
        ]
        

class PeopleSerializer(serializers.ModelSerializer):
    color_id = ColorSerializer()
    class Meta:
        model = Person
        # fields = [
        #     'name',
        #     'age'
        # ]
        fields = "__all__"
        
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError ("Age should be greater than  18")
        return data