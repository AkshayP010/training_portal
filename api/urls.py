from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    # path('employees/', views.EmployeeList.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee-detail'),
    
    
    path("", include(router.urls))
]



