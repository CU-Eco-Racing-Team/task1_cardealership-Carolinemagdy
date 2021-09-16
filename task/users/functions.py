from django.core.exceptions import ObjectDoesNotExist
from users.models import *
from multipledispatch import dispatch

@dispatch(int)
def check_dealer_exists(id):
    dealer=None
    bool= False
    try:
        # check if the dealer exists
        dealer = User.objects.get(id=id, user_type=2)
        bool= True
    except ObjectDoesNotExist:
        dealer=None
        bool= False
    return bool, dealer  
@dispatch(int,str,int)
def check_dealer_exists(SSN, username, phone_number):
    dealer=None
    bool= False
    try:
        # check if the dealer exists
        
        dealer = User.objects.get(SSN=SSN, username=username,
                                  phone_number=phone_number, user_type=2)
        bool= True
    except ObjectDoesNotExist:
        dealer=None
        bool= False
    return bool, dealer  

