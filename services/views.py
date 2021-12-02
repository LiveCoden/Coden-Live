from django.http.response import HttpResponse
from django.shortcuts import redirect, render

def index(request):
   return render(request, 'services/index.html')

def contact_post(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      message = request.POST.get('message')
      print(name, email, message)
   return redirect('services_main')

