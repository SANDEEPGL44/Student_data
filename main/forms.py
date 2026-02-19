from django import forms
<<<<<<< HEAD
from .models import Student, Course
=======
from .models import Student
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
<<<<<<< HEAD
        fields = ['name', 'age', 'course']

    # 🔥 VERY IMPORTANT
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Select Course"
    )
=======
        fields = '__all__'
>>>>>>> 44d0765888239cd01da4a5d0a5d9bfe30a5bd489
