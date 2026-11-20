from django.contrib import admin
from .models import Course, Student, Book

admin.site.register(Course)
admin.site.register(Student)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('author',)