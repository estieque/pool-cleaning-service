from django.shortcuts import render

from SubsEmail.models import EmailSubs

# Create your views here.
def email(request):
    if request.method=="POST":
        n_email=request.POST.get('n_email')
        en=EmailSubs(n_email=n_email,)
        en.save()
    return render(request, 'index.html', )