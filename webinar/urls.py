from django.urls import path
from . import views

urlpatterns = [
    path('frontend', views.frontend, name='web_frontend'),
    path('frontend/post', views.frontend_post, name='web_frontend_post'),


]