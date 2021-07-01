from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='courses'),
    path('<course_name>', views.course, name='course'),

]