from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from employees.models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404
from rest_framework import mixins, generics, viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EmployeeFilter


# class EmployeeList(APIView):

#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetail(APIView):

#     def get_object(self, pk):
#         return get_object_or_404(Employee, pk=pk)

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         if not employee:
#             return Response(
#                 {"error": "Employee not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         employee=self.get_object(pk)
#         serializer=EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(
#             {"message": "Employee deleted successfully"},
#             status=status.HTTP_204_NO_CONTENT
#         )

# MIXINS       
# class EmployeeList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
    
#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
    
# Generics

# class EmployeeList(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# VIEWSETS
# class EmployeeViewset(viewsets.ViewSet):
#     def list(self, request):
#         employee=Employee.objects.all()
#         serializer=EmployeeSerializer(employee, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     def retrieve(self, request, pk):
#         employee=get_object_or_404(Employee, pk=pk)
#         serializer=EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk):
#         employee=get_object_or_404(Employee, pk=pk)
#         serializer=EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors)
    
#     def delete(self, request, pk):
#         employee=get_object_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    filterset_class=EmployeeFilter
    filter_backends=[SearchFilter, DjangoFilterBackend]
    search_fields=['name']
   
    
        
