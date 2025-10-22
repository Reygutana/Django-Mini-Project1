from django.contrib import admin
from django.urls import path

from employees.views import employee


urlpatterns = [
    path('', employee.dashboard),
]
