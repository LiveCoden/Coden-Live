from django.contrib import admin, sitemaps
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from landing.sitemaps import StaticViewSiteMap
from courses.sitemaps import StaticViewSiteMap as courses
from accounts.sitemaps import StaticViewSiteMap as accounts
from courses.sitemaps import SingleStaticViewSiteMap as course

sitemaps = {
      
      'landing': StaticViewSiteMap,
      'courses': courses,
      'course': course,
      'accounts': accounts,


}

urlpatterns = [

    path('webinar/', include("webinar.urls")),
    path('compiler/', include("compiler.urls")),
    path('demo/', include("demoform.urls")),
    path('account/', include("accounts.urls")),
    path('accounts/', include('allauth.urls')),
    path('', include('landing.urls',),),
    path('courses/', include('courses.urls')),
    path('admin/', admin.site.urls), 
    path('blogs/', include("blogs.urls")),
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('sitemaps.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
         path('summernote/', include('django_summernote.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
