from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Welcome to Django!")

def student_view(request, student_id):
    return HttpResponse(f"The student ID is: {student_id}")