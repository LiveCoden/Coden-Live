from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSiteMap(sitemaps.Sitemap):
    priority = 0.64
    changefreq = 'weekly'
    protocol = "https"

    def items(self):

        return  [
              'register',
              'login',
              'reset_password'          
        ]

    def location(self,item):
        return reverse(item)
