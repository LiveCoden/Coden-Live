from django.contrib import sitemaps
from django.urls import reverse
from .models import Course

class StaticViewSiteMap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):

       return Course.objects.all()

    def location(self,obj):
        return '/courses/%s' % (obj.url_name)
