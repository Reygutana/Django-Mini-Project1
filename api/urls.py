from django.urls import path
from api.view import student_function_base_view, employee_function_base_view, student_class_base_view, employee_class_base_view, employee_mixins
from api.view.student_mixins import StudentsListCreateView, StudentDetailView 
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
    path('cbv-employees/', employee_class_base_view.EmployeeListView.as_view(), name='employee-class-view'),
    path('cbv-employee/<int:employee_id>/', employee_class_base_view.EmployeeDetailView.as_view(), name='employee-class-detail'),

    path('mixins_employees/', employee_mixins.Employees.as_view(), name='employee_mixins_view'),
    path('mixins_employee_detail/<int:pk>/', employee_mixins.Employee.as_view(), name='employee_mixins_detail'),

    # Student mixin views
    path('mixins_students/', StudentsListCreateView.as_view(), name='student_mixins_list_create'),
    path('mixins_student/<int:pk>/', StudentDetailView.as_view(), name='student_mixins_detail'),

]