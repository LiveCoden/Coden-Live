from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSiteMap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'weekly'
    protocol = "https"

    def items(self):

        return  [
              'index',
              'compiler'          
        ]

    def location(self,item):
        return reverse(item)
