from django.shortcuts import render
from students.models import Students
from ..serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def studentView(request):
    if(request.method == 'GET'):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        print(students, serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method == 'POST'):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if(request.method == 'DELETE'):
        student_id = request.data.get('id')
        if not student_id:
            return Response(
                {'error': 'Student ID is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            student = Students.objects.get(id=student_id)
            student.delete()
            return Response(
                {'message': 'Student deleted successfully'}, 
                status=status.HTTP_200_OK
            )
        except Students.DoesNotExist:
            return Response(
                {'error': 'Student not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )


@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    """Handle individual student operations by ID"""
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(
            {'error': 'Student not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(
            {'message': 'Student deleted successfully'}, 
            status=status.HTTP_200_OK
        )
