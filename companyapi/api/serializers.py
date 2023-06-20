from rest_framework import serializers
from api.models import Company, Employee

# Create Serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()  # Read-only field for the company_id

    class Meta:
        model = Company
        fields = "__all__"  # Include all fields from the Company model

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()  # Read-only field for the id

    class Meta:
        model = Employee
        fields = "__all__"  # Include all fields from the Employee model