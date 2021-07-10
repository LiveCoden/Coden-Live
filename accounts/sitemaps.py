from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSiteMap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):

        return  [
              'register',
              'login',
              'reset_password'          
        ]

    def location(self,item):
        return reverse(item)
