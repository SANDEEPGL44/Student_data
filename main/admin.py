from django.contrib import admin
<<<<<<< HEAD
from .models import Student, Course, Teacher

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
=======
from .models import Course, Student

admin.site.register(Course)
admin.site.register(Student)
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489
