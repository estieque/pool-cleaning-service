from django.db import models

# Create your models here.
class EmailSubs(models.Model):
    email_id = models.AutoField(primary_key=True)
    n_email = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.n_email