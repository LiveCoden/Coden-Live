from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from .models import DemoForm
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.html import strip_tags
from courses.models import Course

def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        phone = request.POST['phone']
        type = request.POST['type']
        if type == "navform":
            url_name = ""
            demo = DemoForm(name=name, email=email, course=course, phone=phone)
            demo.save()

            subject = 'Subject'
            html_message = render_to_string('mail.html', context=
                                            {"course":course,
                                            "name":name,
                                            "url":url_name,
                                            })
            plain_message = strip_tags(html_message)
    
            print("ww")
            send_mail(
            subject= 'Regrading Course Demo',
                html_message= html_message,
                message=plain_message,
                from_email= 'livecoden@gmail.com',
                recipient_list= [email],
                fail_silently=False,
            )

            messages.success(
                request, " We will get back to you, Your request has been submitted.")

            return redirect('/courses/' )

        else:

            url_name = Course.objects.get(name=course).url_name


            demo = DemoForm(name=name, email=email, course=course, phone=phone)
            demo.save()

            subject = 'Subject'
            html_message = render_to_string('mail.html', context=
                                            {"course":course,
                                            "name":name,
                                            "url":url_name,
                                            })
            plain_message = strip_tags(html_message)
    

            send_mail(
            subject= 'Regrading Course Demo',
                html_message= html_message,
                message=plain_message,
                from_email= 'livecoden@gmail.com',
                recipient_list= [email],
                fail_silently=False,
            )

            messages.success(
                request, " We will get back to you, Your request has been submitted.")

        return redirect('/courses/' + url_name )
