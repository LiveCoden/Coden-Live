from django.shortcuts import get_object_or_404, render
from .models import Course

def index(request):
    courses = Course.objects.all()
    
    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)


def course(request, course_name):

    course = get_object_or_404(Course, url_name=course_name)
    context = {
        'course': course
    }
    return render(request, 'courses/course.html', context)    