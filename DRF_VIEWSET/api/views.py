from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


class StudentViewSet(viewsets.ViewSet):
    
    def list(self, request):
        stu = Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        if pk is not None:       
            stu= Student.objects.get(id=pk)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student saved successfully!'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        stu = Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student updated successfully!'}
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        stu = Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'student updated partially successfull!'}
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        stu = Student.objects.get(id=pk)
        stu.delete()
        res={'msg':'data deleted successfully!'}
        return Response(res)
