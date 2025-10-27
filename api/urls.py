from rest_framework.routers import DefaultRouter

from django.urls import path, include
from api.view import student_function_base_view, employee_function_base_view, student_class_base_view, employee_class_base_view, employee_mixins, student_generic
from api.view.student_mixins import StudentsListCreateView, StudentDetailView 
from api.view import employee_generic
from api.view import employee_viewset
from api.view import student_viewset

router = DefaultRouter()
router.register('viewsets-employees', employee_viewset.Employees, basename='viewsets-employees')
router.register('model-viewsets-employees', employee_viewset.EmployeeModelViewSet)

router.register('viewsets-students', student_viewset.StudentsViewSet, basename='viewsets-students')
router.register('model-viewsets-students', student_viewset.StudentModelViewSet)
urlpatterns = [
    # Function-based views - List views (GET all, POST new, DELETE with id in body)
    path('fbv_students/', student_function_base_view.studentView),
    path('fbv_employees/', employee_function_base_view.employeeView),
    
    # Function-based views - Detail views (GET one, PUT update, DELETE by URL)
    path('fbv_students/<int:pk>/', student_function_base_view.studentDetailView),
    path('fbv_employees/<int:pk>/', employee_function_base_view.employeeDetailView),

    # Class-based views - Students
    path('cbv-students/', student_class_base_view.StudentListView.as_view(), name='student-class-view'),
    path('cbv-student/<int:student_id>/', student_class_base_view.StudentDetailView.as_view(), name='student-class-detail'),
    
    # Class-based views - Employees
    path('cbv_employees/', employee_class_base_view.Employee.as_view(), name='employee-class-view'),
    path('cbv_employee_details/<int:employee_id>/', employee_class_base_view.EmployeeDetailView.as_view(), name='employee-class-detail'),

    path('mixins_employees/', employee_mixins.Employees.as_view(), name='employee_mixins_view'),
    path('mixins_employees/<int:pk>/', employee_mixins.Employee.as_view(), name='employee_mixins_detail'),

    # Student mixin views
    path('mixins_students/', StudentsListCreateView.as_view(), name='student_mixins_list_create'),
    path('mixins_student/<int:pk>/', StudentDetailView.as_view(), name='student_mixins_detail'),

    path('generic_employee/', employee_generic.Employees.as_view()),
    path('generic_employee_details/<int:pk>', employee_generic.EmployeeDetails.as_view()),

    path('generic_students/', student_generic.StudentsList.as_view()),
    path('generic_student_details/<int:pk>', student_generic.StudentDetails.as_view()),

    path('', include(router.urls)),
]