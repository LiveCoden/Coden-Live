from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compiler', views.compiler, name='compiler'),
    # path('sitemap.xml', views.sitemap),
    path('robots.txt', views.robot)  ,
        path('script', views.script, name='script'),
                path('get', views.script_get, name='get'),


]