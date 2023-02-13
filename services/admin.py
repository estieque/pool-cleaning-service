from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Services
# Register your models here.
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('title','image_tag',)
    search_fields = ('title',)
    
    
admin.site.register(Services, ServiceAdmin)
    