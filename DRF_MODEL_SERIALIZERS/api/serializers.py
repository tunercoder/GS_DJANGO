from ast import Delete
from wsgiref.validate import validator
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Student

#VALIDATORS PRIORITY IS FUNCTION BASED THEN FIELD BASED AND THEN OBJECT LEVEL 
# function based reusable validatiors  used as reusbale components any where in your code 
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('value supplied must start with r !')
    return value



class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
    name=serializers.CharField(validators=[starts_with_r])
    class Meta:
        model=Student
        fields=['id','name','roll','city']
        # read_only_fields=['name','roll']
        # extra_kwargs={'name':{'read_only':True}}

    
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
