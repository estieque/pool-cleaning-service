from django.shortcuts import render

from homepage.models import Apointment

# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        service=request.POST.get('service')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        en=Apointment(name=name,email=email,service=service,phone=phone,message=message,)
        en.save()
    return render(request, 'contact.html', )
