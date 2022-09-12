from email.generator import DecodedGenerator
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from api import serializers
from django.views.decorators.csrf import csrf_exempt



def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    print(stu)
    serialized=StudentSerializer(stu)
    print(serialized)
    print(type(serialized.data))
    # json_data=JSONRenderer().render(serialized.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serialized.data,safe=False)


def student_all(request):
    stu = Student.objects.all()
    serialized=StudentSerializer(stu,many=True)
    json_data=JSONRenderer().render(serialized.data)
    return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def student_create(request):
    #serializer me create method define karngeg for savinf data to DB model
    # request.body se posted data lenge
    # iobuffer se stream lenge 
    # stream ka data ko parser me pass karke json se python type me 
    # serializer class me data = parsed data deke is_valid se validate karenge
    # agar validate hogya to save kar denge and response return kar denge else serialzer.error as response  return kar DecodedGenerator
    json_data=request.body
    stream=io.BytesIO(json_data)
    python_data=JSONParser().parse(stream)
    serializer=serializers.StudentSerializer(data=python_data)
    if serializer.is_valid():
        serializer.save()
        res={'msg':'data saved successfully!'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res)
    return JsonResponse(serializer.errors)
