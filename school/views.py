from django.shortcuts import render
from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.order_by(ordering).all()
    context = {'students': students}
    return render(request, template, context)
