from django.shortcuts import render
from project.permissions import *
from .functions import *
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view(['POST', 'DELETE'])
@permission_classes((IsAuthenticated,IsOwner))
def can_sign_a_contract_permission(request, id): 
    # the owner gives or removes the permission to a dealer to sign a contract
    
    #   check the existence of such a dealer 
    exists, dealer = check_dealer_exists(id)
    if not exists:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    # check if the dealer alredy has the permission 
    has_perm = dealer.has_perm('users.can_sign_a_contract') 
    #   POST
    if request.method == 'POST':
        if has_perm :
            return Response({'error': 'dealer already can sign a contract'},
                            status=status.HTTP_400_BAD_REQUEST)
        # if he doesn't have it we should add it to his permissions
        else:
            dealer.user_permissions.add('can_sign_a_contract')
            dealer.save()
            return Response(status=status.HTTP_200_OK)
    #   DELETE
    elif request.method == 'DELETE':
        if not has_perm :
            return Response({'error': 'dealer already can not sign a contract'},
                            status=status.HTTP_400_BAD_REQUEST)
        # if he has it we should remove it from his permissions
        else:
            dealer.user_permissions.remove('can_sign_a_contract')
            dealer.save()
            return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'DELETE'])
@permission_classes((IsAuthenticated,IsOwner))
def can_sell_permission(request, id): 
    # the owner gives or removes the permission to a dealer to sell a car to customer
    
    #   check the existence of such a dealer 
    exists, dealer = check_dealer_exists(id)
    if not exists:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    # check if the dealer alredy has the permission 
    has_perm = dealer.has_perm('users.can_sell_a_car') 

    #   POST
    if request.method == 'POST':
        if has_perm :
            return Response({'error': 'dealer already can sell a car'},
                            status=status.HTTP_400_BAD_REQUEST)
        # if he doesn't have it we should add it to his permissions        
        else:
            dealer.user_permissions.add('can_sell_a_car')
            dealer.save()
            return Response(status=status.HTTP_200_OK)
    #   DELETE
    elif request.method == 'DELETE':
        if not has_perm :
            return Response({'error': 'dealer already can not sell a car'},
                            status=status.HTTP_400_BAD_REQUEST)
        # if he has it we should remove it from his permissions
        else:
            dealer.user_permissions.remove('can_sell_a_car')
            dealer.save()
            return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'DELETE'])
@permission_classes((IsAuthenticated,IsOwner))
def can_change_a_car_price_permission(request, id): 
    # the owner gives or removes the permission to a dealer to change a car's price 
    
    #   check the existence of such a dealer 
    exists, dealer = check_dealer_exists(id)
    if not exists:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    # check if the dealer alredy has the permission 
    has_perm = dealer.has_perm('users.can_change_a_car_price') 

    #   POST
    if request.method == 'POST':
        if has_perm :
            return Response({'error': 'dealer already can change a car price'},
                            status=status.HTTP_400_BAD_REQUEST)
        # if he doesn't have it we should add it to his permissions        
        else:
            dealer.user_permissions.add('can_change_a_car_price')
            dealer.save()
            return Response(status=status.HTTP_200_OK)
    #   DELETE
    elif request.method == 'DELETE':
        if not has_perm :
            return Response({'error': 'dealer already can not change a car price'},
                            status=status.HTTP_400_BAD_REQUEST)
         # if he has it we should remove it from his permissions
        else:
            dealer.user_permissions.remove('can_change_a_car_price')
            dealer.save()
            return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'DELETE'])
@permission_classes((IsAuthenticated,IsOwner))
def can_buy_a_car_permission(request, id): 
    # the owner gives or removes the permission to a dealer to buy a car 
    
    #   check the existence of such a dealer 
    exists, dealer = check_dealer_exists(id)
    if not exists:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    # check if the dealer alredy has the permission 
    has_perm = dealer.has_perm('users.can_buy_a_car') 

    #   POST
    if request.method == 'POST':
        if has_perm :
            return Response({'error': 'dealer already can buy a car'},
                            status=status.HTTP_400_BAD_REQUEST)
        # if he doesn't have it we should add it to his permissions        
        else:
            dealer.user_permissions.add('can_buy_a_car')
            dealer.save()
            return Response(status=status.HTTP_200_OK)
    #   DELETE
    elif request.method == 'DELETE':
        if not has_perm :
            return Response({'error': 'dealer already can not buy a car'},
                            status=status.HTTP_400_BAD_REQUEST)
        # if he has it we should remove it from his permissions
        else:
            dealer.user_permissions.remove('can_buy_a_car')
            dealer.save()
            return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,IsOwner))
def change_owner(request, id): 
    # the owner passes his position to the dealer then he will be deleted
    
    #   check the existence of such a dealer 
    exists, dealer = check_dealer_exists(id)
    if not exists:
        return Response(status=status.HTTP_404_NOT_FOUND)     
    User = request.user
    # delete the owner
    User.delete()
    # set the type of the dealer to 1 to promote him to owner 
    dealer.user_type= 1
    dealer.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,IsOwner))
def remove_a_dealer (request, id):
    #  remove a dealer by the owner 

    #   check the existence of such a dealer 
    exists, dealer = check_dealer_exists(id)
    if not exists:
        return Response(status=status.HTTP_404_NOT_FOUND)  
    else:
        dealer.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,IsOwner))
def add_a_dealer (request):
    # add a dealer by the owner 

    SSN=request.data["SSN"]
    username=request.data["username"]
    phone_number=request.data["phone_number"]
    
    #   check the existence of such a dealer 
    exists, _ = check_dealer_exists(SSN,username,phone_number)
        
    # put a flag to see whether the dealer already exists
    if exists:
        return Response({'error': 'dealer already exists'},
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        # pass all the info from request data to create a dealer set the data type to 2
        User.objects.create_user(SSN, username, phone_number,2)
        return Response(status=status.HTTP_201_CREATED)



