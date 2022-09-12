from ast import Delete
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(request,validate_data):
        return Student.objects.create(**validate_data)

    