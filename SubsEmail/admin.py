from django.contrib import admin

from SubsEmail.models import EmailSubs

# Register your models here.
class EmailSubsAdmin(admin.ModelAdmin):
    list_display = ('n_email', 'add_date')

admin.site.register(EmailSubs, EmailSubsAdmin)