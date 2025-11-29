from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('courses/', views.courses_view, name='courses'),
    path('trainers/', views.trainers_view, name='trainers'),
    path('students/', views.students_view, name='students'),
    path('add/student/', views.add_student, name='add_student'),
    path('add/trainer/', views.add_trainer, name='add_trainer'),

    path('trainers/<int:id>/', views.trainer_detail, name='trainer_detail'),    
    path('trainers<int:id>/edit/', views.trainer_edit, name='trainer_edit'),    
    path('trainers<int:id>/delete/', views.trainer_delete, name='trainer_delete'),
    
    
path('students/<int:id>/', views.student_detail, name='student_detail'),
path('students<int:id>/edit/', views.student_edit, name='student_edit'),
path('students<int:id>/delete/', views.student_delete, name='student_delete'),

path('courses/<int:id>/', views.course_detail, name='course_detail'),
path('courses<int:id>/edit/', views.course_edit, name='course_edit'),
path('courses<int:id>/delete/', views.course_delete, name='course_delete'),
 ]
