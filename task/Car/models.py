from Industry.models import Industry
from django.db import models
from users.models import *
# Create your models here.



class Car(models.Model):
    # Customer who bought the car, one customer has many cars
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customer_cars',null=True)
    # Industry who made the car, one Industry has many cars
    industry = models.ForeignKey(
        Industry, on_delete=models.CASCADE, related_name='industry_cars',null=True)    
    # model of each car
    model =models.CharField(max_length=100,)
    # plate number of each car
    plate_number = models.PositiveIntegerField(default=0)
    # price of each car
    price = models.PositiveIntegerField(default=0)
    # payment methon either cash or installment
    CASH = 'C'
    INSTALLMENT = 'I'
    PAYMENT_METHOD = [
        (CASH, 'Cash'),
        (INSTALLMENT, 'Installment'),
    ]
    payment = models.CharField(max_length=1, choices=PAYMENT_METHOD, default=CASH,)

    def __str__(self):
        return self.model
        

# m = Car.objects.filter(payment=Car.CASH)

