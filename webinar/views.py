from django.contrib import messages
from django.shortcuts import redirect, render
import gspread

gc = gspread.service_account(filename='key.json')
sh = gc.open_by_key('1XzOkuTBUVdj8Wdm_y4GbLK5Bo4KUNZS5iSCiLTGqQ18')
worksheet = sh.sheet1


def webinar(request):
   
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSfbBtmllLAMtXsI3Bi-e9SrrFAX1JOnqXsVPAaBYYle5Ujq_w/viewform')
 

   
