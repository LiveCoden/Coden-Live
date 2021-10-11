from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webinar(request):

    if(request.method) == 'POST':
        code = request.GET["code"]
        print(code)
        if(code=="748"):
            return JsonResponse("{check : yes}", safe=False)
        else:
            return JsonResponse("{check : no}", safe=False)

   
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSfbBtmllLAMtXsI3Bi-e9SrrFAX1JOnqXsVPAaBYYle5Ujq_w/viewform')
 

   
