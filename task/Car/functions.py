from django.core.exceptions import ObjectDoesNotExist
from users.models import *
from .models import *

def check_car_availability(id):
    car=None
    bool= False
    try:
        # check if the Car exists and it is not assigned  to any customer 
        car = Car.objects.get(id=id , customer=None)
        bool= True
    except ObjectDoesNotExist:
        car=None
        bool= False
    return bool, car

def check_car_exists(id):
    car=None
    bool= False
    try:
        # check if the Car already exists in the shop
        car = Car.objects.get(id=id)
        bool= True
    except ObjectDoesNotExist:
        car=None
        bool= False
    return bool, car

def check_customer_exists(id):
    customer=None
    bool= False
    try:
        # check if the Customer exists
        customer = User.objects.get(id=id, user_type=3)
        bool= True
    except ObjectDoesNotExist:
        customer=None
        bool= False
    return bool, customer 
  
def check_industry_exists(id):
    industry=None
    bool= False
    try:
        # check if the Industry exists
        industry = Industry.objects.get(id=id)
        bool= True
    except ObjectDoesNotExist:
        industry=None
        bool= False
    return bool, industry   