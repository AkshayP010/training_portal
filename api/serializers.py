import re
from rest_framework import serializers
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def validate_emp_id(self, value):
        if not re.match(r'^EMP[0-9]+$', value):
            raise serializers.ValidationError(
                "emp_id must be in the format EMP followed by numbers (e.g., EMP001)"
            )
        return value

    def validate_email(self, value):
        if not value.endswith('@company.com'):
            raise serializers.ValidationError(
                "Email must be from @company.com domain"
            )
        return value

    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Salary must be a positive number"
            )
        return value
