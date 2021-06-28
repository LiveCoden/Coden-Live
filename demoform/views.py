from django.shortcuts import redirect, render
from .models import DemoForm
from django.contrib import messages
from django.core.mail import send_mail

def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        phone = request.POST['phone']
        id = request.POST['id']

        demo = DemoForm(name=name,email=email,course=course,phone=phone)
        demo.save()
        send_mail(
        'Subject here',
        'Here is the message.',
        'livecoden@gmail.com',
        ['chetankhanna767@gmail.com'],
        fail_silently=False,
)

        messages.success(request, " We will get back to you, Your request has been submitted.")
       

    return redirect('/courses/' + id)