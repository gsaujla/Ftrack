from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TYPE =(
   ('Yes','Yes'),
   ('No','No'),
)

class profile(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    income = models.IntegerField()
    balance = models.FloatField(null = True , default = income , blank = True)
    expenditure = models.FloatField(default = 0, null = True , blank = True)




class activity(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    description = models.CharField(max_length = 150)
    amount = models.FloatField()
    gainornot = models.CharField(max_length = 100 , choices = TYPE , default = "No" , null = True)

    def __str__(self):
        return self.description
    

 
  