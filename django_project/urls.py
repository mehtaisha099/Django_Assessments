from django.contrib import admin
from django.urls import path
from myapp.views import home, student_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('student/<int:student_id>/', student_view),
]