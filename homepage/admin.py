from django.contrib import admin

from homepage.models import Apointment

# Register your models here.
class ApointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'message', 'add_date')

admin.site.register(Apointment, ApointmentAdmin)