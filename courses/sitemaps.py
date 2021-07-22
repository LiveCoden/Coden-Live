from django.contrib import sitemaps
from django.urls import reverse
from .models import Course

class StaticViewSiteMap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    protocol = "https"

    def items(self):

       return  Course.objects.all()

    def location(self,obj):
        return '/courses/%s' % (obj.url_name)


class SingleStaticViewSiteMap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    protocol = "https"

    def items(self):

       return  ['courses']

    def location(self,item):
        return reverse(item)