from django.urls import path
from . import views

urlpatterns = [
    path('', views.services,),
        path('robots.txt', views.robot)  ,
                path('Best-digital-marketing-company-in-Delhi-NCR', views.index, name='services_main')  ,


    path('contact_post', views.contact_post, name='contact_post'),

]