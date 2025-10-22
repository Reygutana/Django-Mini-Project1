from rest_framework import mixins, generics
from ..serializer import StudentSerializer
from students.models import Students  # This is the model

class StudentsListCreateView(  # <-- renamed to avoid clash
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StudentDetailView(  # <-- renamed to avoid clash
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
