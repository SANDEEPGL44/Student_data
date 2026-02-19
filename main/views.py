<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import Student, Course
from .forms import StudentForm


# ---------------- HOME ----------------
def home(request):
    return render(request, 'home.html')


# ---------------- FBV – STUDENT LIST ----------------
def student_list(request):

    # Base queryset with ordering (CHANGE HERE if needed)
    students = Student.objects.all().order_by("id")  
    # Options:
    # .order_by("id")     → Oldest first
    # .order_by("-id")    → Newest first
    # .order_by("name")   → Alphabetical
    # .order_by("age")    → Age order

    # Filtering by course
    course_id = request.GET.get("course")
    if course_id:
        students = students.filter(course_id=course_id)

    # Pagination (5 per page)
    paginator = Paginator(students, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    courses = Course.objects.all()

    return render(request, "students/list.html", {
        "page_obj": page_obj,
        "courses": courses
    })


# ---------------- FBV – STUDENT DETAIL ----------------
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/detail.html", {"student": student})


# ---------------- FBV – ADD STUDENT ----------------
def add_student(request):

=======
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course

def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})


def add_student(request):
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        course_id = request.POST.get("course")

<<<<<<< HEAD
        Student.objects.create(
            name=name,
            age=age,
            course_id=course_id
        )

        return redirect("students")

    courses = Course.objects.all()

    return render(request, "students/add.html", {
        "courses": courses
    })


# ---------------- FBV – EDIT STUDENT ----------------
def student_edit(request, id):
=======
        course = Course.objects.get(id=course_id)

        Student.objects.create(name=name, age=age, course=course)
        return redirect("students")

    courses = Course.objects.all()
    return render(request, "add_student.html", {"courses": courses})


def edit_student(request, id):
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.course_id = request.POST.get("course")
        student.save()
<<<<<<< HEAD

        return redirect("students")

    courses = Course.objects.all()

    return render(request, "students/edit.html", {
=======
        return redirect("students")

    courses = Course.objects.all()
    return render(request, "edit_student.html", {
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489
        "student": student,
        "courses": courses
    })


<<<<<<< HEAD
# ---------------- FBV – DELETE STUDENT ----------------
def student_delete(request, id):
=======
def delete_student(request, id):
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()

    return redirect("students")

<<<<<<< HEAD

# ---------------- CBV – COURSE LIST ----------------
class CourseListView(ListView):
    model = Course
    template_name = "courses/list.html"
    queryset = Course.objects.all().order_by("id")


# ---------------- CBV – COURSE DETAIL ----------------
class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
=======
def home(request):
    return render(request, 'home.html')
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489
