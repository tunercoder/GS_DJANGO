from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def stuapi(request,pk=None):

    if request.method == 'GET':
        id= pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    


    if request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student saved successfully!'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id= pk
        stu = Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student updated successfully!'}
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PUT':
        id= pk
        stu = Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student updated successfully!'}
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        id= pk
        stu = Student.objects.get(id=id)
        stu.delete()
        res={'msg':'student deleted successfully!'}
        return Response(res)

