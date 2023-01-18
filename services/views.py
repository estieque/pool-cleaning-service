from django.shortcuts import render

# Create your views here.
def services(request, slug_url):
    print(slug_url)
    return render(request, 'services.html', {'services' : 'Pool Cleaning'} )

def servicess(request):
    return render(request, 'servicess.html', {'services' : 'Pool Cleaning'} )