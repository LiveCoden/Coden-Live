from django.contrib import messages
from django.shortcuts import redirect, render
import gspread

gc = gspread.service_account(filename='key.json')
sh = gc.open_by_key('1XzOkuTBUVdj8Wdm_y4GbLK5Bo4KUNZS5iSCiLTGqQ18')
worksheet = sh.sheet1


def frontend(request):
   
    return render(request, 'webinar/frontend.html')


def frontend_post(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        how = request.POST.get('how')
        worksheet.append_row([name, email, number, how])
        messages.success(request, 'Thank you for your submission!')
        return redirect('web_frontend')    

   
