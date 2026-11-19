from django.http import HttpResponse
from django.db.models import Avg
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Student, Book


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


def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})


class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = Book.objects.count()
        return context


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('book-list')