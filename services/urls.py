from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='services_main'),
        path('robots.txt', views.robot)  ,

    path('contact_post', views.contact_post, name='contact_post'),

]