from rest_framework import mixins, generics
from ..serializer import EmployeeSerializer
from employees.models import Employee


class Employees(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class Employee(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get (self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)