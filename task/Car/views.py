from Industry.serializers import IndustrySerializer
from Car.serializers import *
from django.shortcuts import render
from .models import *
from users.models import *
from users.views import *
from .functions import *
# Create your views here.
@api_view(['POST'])
@permission_classes((IsAuthenticated,IsOwnerOrDealer))
def sell_car(request, carid,custid ):
    user=request.user
    #   check if a dealer has a permission to sell a car
    has_perm = user.has_perm('users.can_sell_a_car') 
    if not (has_perm or user.OWNER):
        return Response(status=status.HTTP_403_FORBIDDEN)
    # check if the car available or sold
    exists, car = check_car_availability(carid)
    if not exists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # check if it is an old customer or we should create new one 
    exists, customer = check_customer_exists(custid)
    if not exists:
        SSN=request.data["SSN"]
        username=request.data["username"]
        phone_number=request.data["phone_number"]
        # pass all the info from request data to create Customer set the data type to 3
        User.objects.create_user(SSN, username, phone_number,3)
        customer=User.objects.get(SSN = SSN)
    # add the car to the customer 
    customer.customer_cars.add(car)
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes((IsAuthenticated,IsOwnerOrDealer))
def buy_car(request, carid,industid):
    
    user=request.user
    #   check if a dealer has a permission to buy a car

    has_perm = user.has_perm('users.can_buy_a_car') 
    if not (has_perm or user.OWNER):
        return Response(status=status.HTTP_403_FORBIDDEN)
    # check if the car already exists in the shop 
    exists, _ = check_car_exists(carid)
    if exists:
        return Response({'error': 'Car already exists in the shop'},
                status=status.HTTP_400_BAD_REQUEST)

    # check if it is an old industry or we should create new one 
    exists, industry = check_industry_exists(industid)
    if not exists:
        serializer = IndustrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    # to buy a new Car we create a new object of a Car in our Shop database        
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(industry=industry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,IsOwnerOrDealer))
def change_price(request, carid):
    
    user=request.user
    #   check if a dealer has a permission to change a car's price
    has_perm = user.has_perm('users.can_buy_a_car') 
    if not (has_perm or user.OWNER):
        return Response(status=status.HTTP_403_FORBIDDEN)
    # check if the car available or sold
    exists, car = check_car_availability(carid)
    if not exists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # edit the price of this car 
    serializer = PriceSerializer(car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)