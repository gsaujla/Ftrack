from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    income = models.IntegerField()
    balance = models.FloatField(null = True)
    expenditure = models.FloatField()




class activity(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    description = models.CharField(max_length = 150)
    amount = models.FloatField()
    
    gain = models.BooleanField() 

    def __str__(self):
        return self.description
    

 
  