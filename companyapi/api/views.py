from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()  # Retrieve all instances of the Company model
    serializer_class = CompanySerializer  # Use the CompanySerializer for serialization

    # Custom API endpoint: companies/{companyID}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            # Retrieve the company based on the provided primary key (pk)
            company = Company.objects.get(pk=pk)

            # Filter employees based on the company
            emps = Employee.objects.filter(company=company)

            # Serialize the employee data
            emp_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Company might not exist! Error'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()  # Retrieve all instances of the Employee model
    serializer_class = EmployeeSerializer  # Use the EmployeeSerializer for serialization