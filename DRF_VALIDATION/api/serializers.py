from ast import Delete
from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student



#VALIDATORS PRIORITY IS FUNCTION BASED THEN FIELD BASED AND THEN OBJECT LEVEL 
# function based reusable validatiors  used as reusbale components any where in your code 
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('value supplied must start with r !')
    return value



class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50,validators=[starts_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(request,validate_data):
        return Student.objects.create(**validate_data)

    
    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.roll=validate_data.get('roll',instance.roll)
        instance.city=validate_data.get('city',instance.city)
        instance.save()
        return instance

#validators on field level

    def validate_roll(self,value):
        if value > 200:
            raise serializers.ValidationError('seats full!')
        return value

#Object level validation when using more than one field validation is required

    def validate(self,data):
        name=data.get('name')
        cityname=data.get('city')
        if name.lower() == 'dhoni' and cityname.lower()!='ranchi':
            raise serializers.ValidationError('for dhoni city must be ranchi!')
        return data

