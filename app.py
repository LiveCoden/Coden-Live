import threading
import urllib3
import bs4

def fetch_url(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = bs4.BeautifulSoup(r.data, 'html.parser')
    try:
        content =  (soup.find("meta",  {"name":"keywords"})['content'])
        list.append(content)

    except:
        print ("No meta keywords")    

    
urls = ["http://www.coden.live", "http://www.hackersvilla.xyz", "http://www.geeksforgeeks.com"]
http = urllib3.PoolManager()
threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    
        thread.start()

for thread in threads:
    
        print(thread.is_alive)    
        print(threading.current_thread().ident)
    

for thread in threads:
    
        thread.join()

for thread in threads:
    
        print(thread.is_alive)    
        print(threading.current_thread().ident)
    


        
