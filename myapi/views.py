from django.shortcuts import render
from myapi.models import Student
from myapi.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter]
    search_fields=['name','city','roll','course','email']
