from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer


class StudentListCreateAPI(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
