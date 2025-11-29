from django import forms
from .models import Course, Trainer, Student

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
