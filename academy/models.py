from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in weeks")
    course_image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return self.course_name


class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=100)
    trainer_photo = models.ImageField(upload_to='trainer_photos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    enrolled_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='students')
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, related_name='students')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    

