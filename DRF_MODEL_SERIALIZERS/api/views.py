from django.shortcuts import render
from django.http import JsonResponse
from .serializers import StudentSerializer
from .models import Student
import io
from rest_framework.parsers import JSONParser
from api import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator


#CLASS BASED APPROACH BY MAKING A CLASS OF VIEW IN DJANGO
@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id= python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serialized=StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serialized=StudentSerializer(stu,many=True)
        
        return JsonResponse(serialized.data,safe=False)
    


    def post(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=serializers.StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student saved successfully!'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)

    def put(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id= python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer=serializers.StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student updated successfully!'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)

    def delete(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id= python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res={'msg':'student deleted successfully!'}
        return JsonResponse(res)

