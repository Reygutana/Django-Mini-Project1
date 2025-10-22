from django.shortcuts import render
from employees.models import Employee
from ..serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def employeeView(request):
    if(request.method == 'GET'):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        print(employees, serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method == 'POST'):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if(request.method == 'DELETE'):
        employee_id = request.data.get('id')
        if not employee_id:
            return Response(
                {'error': 'Employee ID is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()
            return Response(
                {'message': 'Employee deleted successfully'}, 
                status=status.HTTP_200_OK
            )
        except Employee.DoesNotExist:
            return Response(
                {'error': 'Employee not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )


@api_view(['GET', 'PUT', 'DELETE'])
def employeeDetailView(request, pk):
    """Handle individual employee operations by ID"""
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(
            {'error': 'Employee not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(
            {'message': 'Employee deleted successfully'}, 
            status=status.HTTP_200_OK
        )