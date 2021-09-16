from .views import *
from django.urls import path, include
app_name = 'Car'
urlpatterns = [
    # API to sell a car
    path('<int:car_id>/customer/<int:customer_id>', sell_car, name='sell_car'),
    
    # API to buy a car
    path('<int:car_id>/industry/<int:industry_id>', buy_car, name='buy_car'),
    
    # API to change the price of a car
    path('<int:car_id>/price', change_price, name='change_price'),


]
