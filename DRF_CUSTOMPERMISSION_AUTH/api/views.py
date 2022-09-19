from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermission import CustomerAccessPermission
from api import serializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomerAccessPermission]

