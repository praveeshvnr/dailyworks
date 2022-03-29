from django.core import mail
from django.shortcuts import render
from app.models import em
from first.settings import EMAIL_HOST_USER
from django.core.mail import message, send_mail
# Create your views here.


def emm(request):
    return render(request, 'emm.html')
def ema(request):
    member=em(mail=request.POST['mail'],)
    member.save()
    subject='hello'
    message='welcome'
    print(member.mail)
    recepient=str(member.mail)
    send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
    return render(request,'emm.html')