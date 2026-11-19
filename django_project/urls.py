from django.contrib import admin
from django.urls import path
from myapp.views import (
    home,
    student_view,
    adult_students,
    average_age,
    book_list,
    BookListView,
    BookCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('student/<int:student_id>/', student_view),
    path('adult-students/', adult_students),
    path('average-age/', average_age),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add/', BookCreateView.as_view(), name='book-create'),
]