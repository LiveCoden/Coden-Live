import json
from django.contrib import messages
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.http.response import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webinar(request):


    if(request.method) == 'POST':
        data= json.loads(request.body)
        print(data['code'])

        if(data['code']== '3119'):

            return JsonResponse({'flag':'tat@kaE'}, safe=False)
        else:
            return HttpResponseServerError()


 

   
