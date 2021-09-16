from .views import *
from django.urls import path, include
app_name = 'users'
urlpatterns = [
    # API to change the owner of the shop
    path('<int:dealer_id>', change_owner , name='change_owner'),
    # API to remove a dealer from the shop
    path('dealer/<int:dealer_id>', remove_a_dealer , name='remove_a_dealer'),
    # API to add a dealer to the shop
    path('dealer', add_a_dealer, name='add_a_dealer'),
    # API to give or remove a sign contract permission to a dealer 
    path('dealer/<int:dealer_id>/contract-perms', can_sign_a_contract_permission, name='can_sign_a_contract_permission'),
    # API to give or remove a sell permission to a dealer
    path('dealer/<int:dealer_id>/selling-perms', can_sell_permission, name='can_sell_permission'),
    # API to give or remove a buy permission to a dealer
    path('dealer/<int:dealer_id>/buying-perms', can_buy_a_car_permission , name='can_buy_a_car_permission'),  
    # API to give or remove a change price permission to a dealer
    path('dealer/<int:dealer_id>/price-perms', can_change_a_car_price_permission, name='can_change_a_car_price_permission'),

]
