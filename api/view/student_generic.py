from rest_framework import generics
from students.models import Students
from api.serializer import StudentSerializer

# class Employees(generics.ListAPIView, generics.CreateAPIView):
#    queryset = Employee.objects.all()
#    serializer_class = EmployeeSerializer

# Option 2
class StudentsList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

#class EmployeeDetails(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#    queryset = Employee.objects.all()
#    serializer_class = EmployeeSerializer
#    Lookup_field = 'pk'

# Option 2
class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'