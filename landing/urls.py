from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compiler', views.compiler, name='compiler'),
    # path('sitemap.xml', views.sitemap)  

]