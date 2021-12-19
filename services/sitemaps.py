from django.contrib import sitemaps
from django.contrib.sites.models import Site
from django.urls import reverse

class ServicesViewSiteMap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'weekly'
    protocol = "https"
    location = ""

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='services.coden.live', name='services.coden.live')
        return super(ServicesViewSiteMap, self).get_urls(site=site, **kwargs)

    def items(self):

        return  [
       'services_main'        
        ]

    def location(self,item):
        return reverse(item)
