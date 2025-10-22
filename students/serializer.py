from rest_framework import serializers
from students.models import Students

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fialds = "__all__"
        class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'
    