from rest_framework import serializers
from myapi.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','course','email','city','roll']