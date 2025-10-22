from ..serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from students.models import Students
from django.http import Http404

class StudentListView(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
    
class StudentDetailView(APIView):
    def get_object(self, student_id):
        try:
            return Students.objects.get(pk=student_id)
        except Students.DoesNotExist:
            raise Http404
        
    def get(self, request, student_id):
        student = self.get_object(student_id=student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, student_id):
        student = self.get_object(student_id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, student_id):
        student = self.get_object(student_id=student_id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)