from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import gspread

from services.models import ServicesForm



gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1xVR1I6ulDlnjJDVYO_7smWcmDEexZkhEAx23ScF1qFI')
worksheet = sh.sheet1

def index(request):
   return render(request, 'services/index.html')

def services(request):
   return redirect('services_main')    

def contact_post(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get("phone")
      message = request.POST.get('message')
      print(name, email, message)
      try:
         worksheet.append_row([name,email,phone,message])
      except:
         print("error")   

      services_form = ServicesForm(name=name, email=email, phone=phone, message=message)
      services_form.save()   
      
   return redirect('services_main')

def robot(request):
    return render(request,'services_robots.txt',content_type='text')  





