from django.db import models

<<<<<<< HEAD

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
=======
class Course(models.Model):
    title = models.CharField(max_length=100)
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

<<<<<<< HEAD
=======
    def __str__(self):
        return self.name
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489
