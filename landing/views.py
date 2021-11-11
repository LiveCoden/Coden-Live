from typing import final
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import threading
import urllib3
import time
import bs4
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'index.html')

def compiler(request):
    return render(request,'compiler/compiler.html')

def sitemap(request):
    return render(request,'sitemaps.xml',content_type='text/xml')


def robot(request):
    return render(request,'robots.txt',content_type='text')    



def script(request):
    return render(request,'partials/seo.html')



final_list = []
@csrf_exempt
def script_get(request):

    list = []
    if request.method == 'POST':

        website = request.POST['email']
        keyword = request.POST['text']
        i = 0
        urls = [website, website]
        http = urllib3.PoolManager()
        threads = [threading.Thread(target=fetch_url, args=(url,list)) for url in urls]
        for thread in threads:
            
                thread.start()
        
        for thread in threads:
            
               thread.join()

        print(list)
        return JsonResponse(list, safe=False)


def fetch_url(url,list):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = bs4.BeautifulSoup(r.data, 'html.parser')
    try:
        content =  (soup.find("meta",  {"name":"keywords"})['content'])
        list.append(content)

    except:
        print ("No meta keywords")  
         


def setList(list):
    final_list = list
    print(final_list)

def getList():
    return final_list    
