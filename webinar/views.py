from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webinar(request):

    if(request.method) == 'GET':
        code = request.GET["code"]
        
        if(code=="748"):
            return JsonResponse("{'ok':'yes'}", safe=False)
        else:
            return HttpResponseForbidden()

 

   
