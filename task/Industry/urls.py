from .views import *
from django.urls import path, include
app_name = 'Industry'
urlpatterns = [
    # API to sign a contract
    path('<int:industry_id>/dealer/<int:dealer_id>', sign_contract, name='sign_contract'),


]
