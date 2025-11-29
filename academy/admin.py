from django.contrib import admin
from .models import Course, Trainer, Student

class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "course_name", "duration"]
    list_display_links = ["course_name"]
    search_fields = ["course_name"]
    list_filter = ["duration"]
    ordering = ["course_name"]
admin.site.register(Course, CourseAdmin)


class TrainerAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "expertise"]
    list_display_links = ["full_name"]
    search_fields = ["first_name", "last_name", "email"]
    list_filter = ["expertise"]
    ordering = ["first_name"]
admin.site.register(Trainer, TrainerAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "is_active", "enrolled_course", "trainer"]
    list_display_links = ["full_name"]
    search_fields = ["first_name", "last_name", "email"]
    list_filter = ["is_active"]
    ordering = ["-is_active"]
admin.site.register(Student, StudentAdmin)
