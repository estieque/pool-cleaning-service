from django.shortcuts import render
from .models import Services
# Create your views here.
def services(request):
    service= Services.objects.all()
    context = {'service' :service,}
    return render(request, 'services.html',context)

#def servicess(request):
    #return render(request, 'servicess.html', {'services' : 'Pool Cleaning'} )


def services_detail(request, slug_url):
    #served = Services.objects.get(slug=slug_url)
    #homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    #settings = SiteSetting.objects.all()
    #portslider = portfolioSlider.objects.all().order_by('-hslider_id')[:1]
    #context ={'portd':portd,'homeblogs':homeblogs, 'settings':settings, 'portslider':portslider,}
    return render(request, "service-details.html",)