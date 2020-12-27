from django.db import models
from datetime import datetime
# Create your models here.

class Show(models.Model):
    Title =models.CharField(max_length=100,verbose_name="title")
    Network=models.CharField(max_length=30,verbose_name="network")
    Release_date=models.DateField(verbose_name="release_date")
    Description=models.TextField(null=True,blank=True,max_length=200,verbose_name="description")
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        date=self.Release_date.strftime("%b %d, %Y")
        return self.Title+" - "+self.Network+" - "+self.Description+" - "+date
