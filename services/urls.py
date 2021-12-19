from . import views
from django.contrib import admin, sitemaps
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from services.sitemaps import ServicesViewSiteMap as ServicesSitemap

sitemaps = {
      
      'services': ServicesSitemap,

}

urlpatterns = [
    path('', views.services,),
        path('robots.txt', views.robot)  ,
                path('Best-digital-marketing-company-in-Delhi-NCR', views.index, name='services_main')  ,

   path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('sitemaps.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('contact_post', views.contact_post, name='contact_post'),

]