from Car.models import *
from django.db import models
from datetime import datetime
# Create your models here.
from users.models import *

class Industry(models.Model):
    # name of each industry
    name =models.CharField(max_length=100,)
    # phone number of each industry
    phone_number = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name

class Contract(models.Model):

    # the dealer who makes the contract , one dealer can make many contracts
    supervisor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='dealer_contracts')
    # the industry with wich we make the contract , one industry can make many contracts
    industry = models.ForeignKey(
        Industry, on_delete=models.CASCADE, related_name='industry_contracts')   
    # no of cars must be mentioned in the contract     
    cars_count= models.IntegerField(default=0)
    # start date of the contract 
    start_date= models.DateTimeField(default=datetime.now())
    # end date of the contract
    end_date= models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.supervisor + '_' + self.industry        