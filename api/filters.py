import django_filters
from employees.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model=Employee
        fields={
            'designation': ['iexact','icontains'],
            'salary':['exact', 'lt','gt','range'],
            'emp_id':['lt','gt','range']
             }