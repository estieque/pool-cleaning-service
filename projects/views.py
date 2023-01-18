from django.shortcuts import render

# Create your views here.
def projects(request, a):
    print(a)
    return render(request, 'projects.html', {'projects' : 'Pool Cleaning'} )

def projectss(request):
    return render(request, 'projects.html', {'projects' : 'Pool Cleaning'} )