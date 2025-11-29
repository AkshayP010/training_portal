from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Trainer, Student
from .forms import TrainerForm, StudentForm, CourseForm
from django.contrib.auth.decorators import permission_required, login_required


def home_view(request):
    context = {
        "total_courses": Course.objects.all().count(),
        "total_trainers": Trainer.objects.all().count(),
        "total_students": Student.objects.all().count(),
    }
    return render(request, "home.html", context)

def courses_view(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})

@login_required
@permission_required('academy.view_trainer', raise_exception=True)
def trainers_view(request):
    trainers = Trainer.objects.all()
    return render(request, "trainers.html", {"trainers": trainers})

@login_required
@permission_required('academy.view_student', raise_exception=True)
def students_view(request):
    students = Student.objects.select_related("enrolled_course", "trainer").all()
    return render(request, "students.html", {"students": students})

@login_required
@permission_required('academy.add_student', raise_exception=True)
def add_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form=StudentForm()
    return render(request, 'add_student.html', {'form': form})


def add_trainer(request):
    if request.method=='POST':
        form=TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainers')
    else:
        form=TrainerForm()
    return render(request, 'add_trainer.html', {'form': form})




         # ----------------------------------ACTION SECTION-------------------------------------
# TRAINER

@login_required
@permission_required('academy.view_trainer', raise_exception=True)
def trainer_detail(request, id):
    trainer=get_object_or_404(Trainer, id=id)
    return render(request, 'Actions/trainer_detail.html', {'trainer': trainer})

@login_required
@permission_required('academy.change_trainer', raise_exception=True)
def trainer_edit(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    form = TrainerForm(instance=trainer)

    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainers')

    return render(request, 'Actions/trainer_edit.html', {'form': form})

@login_required
@permission_required('academy.delete_trainer', raise_exception=True)
def trainer_delete(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == "POST":
        trainer.delete()
        return redirect('trainers')
    return render(request, 'Actions/trainer_delete.html', {'trainer': trainer})

# STUDENT

@login_required
@permission_required('academy.view_studentdetail', raise_exception=True)
def student_detail(request, id):
    student=get_object_or_404(Student, id=id)
    return render(request, 'Actions/student_detail.html', {'student': student})

@login_required
@permission_required('academy.change_student', raise_exception=True)
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')

    return render(request, 'Actions/student_edit.html', {'form': form})

@login_required
@permission_required('academy.delete_student', raise_exception=True)
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('students')
    return render(request, 'Actions/student_delete.html', {'student': student})


#COURSE

@login_required
@permission_required('academy.view_course', raise_exception=True)
def course_detail(request, id):
    course=get_object_or_404(Course, id=id)
    return render(request, 'Actions/course_detail.html', {'course': course})

@login_required
@permission_required('academy.change_course', raise_exception=True)
def course_edit(request, id):
    course = get_object_or_404(Course, id=id)
    form = CourseForm(instance=course)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')

    return render(request, 'Actions/course_edit.html', {'form': form})

@login_required
@permission_required('academy.delete_course', raise_exception=True)
def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == "POST":
        course.delete()
        return redirect('courses')
    return render(request, 'Actions/course_delete.html', {'courset': course})







