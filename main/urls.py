from django.urls import path
from . import views
<<<<<<< HEAD
from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('', views.home, name='home'),

    path('students/', views.student_list, name='students'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/add/', views.add_student, name='add_student'),

    path('students/edit/<int:id>/', views.student_edit, name='edit_student'),
    path('students/delete/<int:id>/', views.student_delete, name='delete_student'),

    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
=======

urlpatterns = [
    path("students/", views.students, name="students"),
    path("add-student/", views.add_student, name="add_student"),
    path("edit-student/<int:id>/", views.edit_student, name="edit_student"),
    path("delete-student/<int:id>/", views.delete_student, name="delete_student"),
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489
]
