from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def compiler(request):
    return render(request,'compiler/compiler.html')

def sitemap(request):
    return render(request,'sitemaps.xml',content_type='text/xml')


def robot(request):
    return render(request,'robots.txt',content_type='text')    