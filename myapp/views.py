from django.http import HttpResponse
from django.db.models import Avg
from .models import Student


def home(request):
    return HttpResponse("Hello, Welcome to Django!")


def student_view(request, student_id):
    return HttpResponse(f"The student ID is: {student_id}")


def adult_students(request):
    students = Student.objects.filter(age__gte=18)
    student_list = "<br>".join(
        f"{student.name} - {student.age}" for student in students
    )
    return HttpResponse(student_list)


def average_age(request):
    result = Student.objects.aggregate(average_age=Avg('age'))
    return HttpResponse(f"Average age: {result['average_age']}")