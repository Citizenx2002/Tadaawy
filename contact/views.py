from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def contact(request):
    if request.method == 'POST':

        email=request.POST['c_email']
        subject=request.POST['c_subject']
        message=request.POST['c_message']
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
        # print(email)
        # print(subject)
        # print(message)
    
    return render(request,'contact.html',{})
