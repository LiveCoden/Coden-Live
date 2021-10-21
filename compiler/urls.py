from django.urls import path
from . import views

urlpatterns = [
    path('csharp', views.csharp, name='csharp'),
]