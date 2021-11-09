from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import threading
import urllib3
import time
import bs4

def index(request):
    return render(request,'index.html')

def compiler(request):
    return render(request,'compiler/compiler.html')

def sitemap(request):
    return render(request,'sitemaps.xml',content_type='text/xml')


def robot(request):
    return render(request,'robots.txt',content_type='text')    


list = []

def script(request):
  

    urls = ["http://www.coden.live", "http://www.hackersvilla.xyz","http://www.coden.live", "http://www.hackersvilla.xyz","http://www.coden.live", "http://www.hackersvilla.xyz","http://www.coden.live", "http://www.hackersvilla.xyz","http://www.coden.live", "http://www.hackersvilla.xyz","http://www.coden.live", "http://www.hackersvilla.xyz","http://www.coden.live", "http://www.hackersvilla.xyz","http://www.coden.live", "http://www.hackersvilla.xyz","http://www.coden.live", "http://www.hackersvilla.xyz","http://www.coden.live", "http://www.hackersvilla.xyz", ]
    http = urllib3.PoolManager()
    threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return JsonResponse(list, safe=False)


def fetch_url(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = bs4.BeautifulSoup(r.data, 'html.parser')
    try:
        content =  (soup.find("meta",  {"name":"keywords"})['content'])
        list.append(content)

    except:
        print ("No meta keywords")    

