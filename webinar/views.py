from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render


def webinar(request):

    if(request.method) == 'POST':
        code = request.POST['code']
        if(code!=None):
            return JsonResponse("check : correct")
        else:
            return JsonResponse("check : incorrect")

   
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSfbBtmllLAMtXsI3Bi-e9SrrFAX1JOnqXsVPAaBYYle5Ujq_w/viewform')
 

   
