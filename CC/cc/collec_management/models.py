from django.db import models

# Create your models here.

class Collec(models.Model):
    title = models.CharField(max_length=100, null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    date_creation = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.title
    
    