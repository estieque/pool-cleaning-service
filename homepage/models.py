from django.db import models

# Create your models here.
class Apointment(models.Model):
    appoint_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    service = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.name