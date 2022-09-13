from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer


class StuApi(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student saved successfully!'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk,  format=None):
        stu = Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student updated successfully!'}
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk,  format=None):
        stu = Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student updated successfully!'}
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk,  format=None):
        stu = Student.objects.get(id=pk)
        stu.delete()
        res={'msg':'student deleted successfully!'}
        return Response(res)

