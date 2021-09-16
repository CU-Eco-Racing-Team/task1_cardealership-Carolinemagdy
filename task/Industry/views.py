from django.shortcuts import render
from users.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from Car.functions import *
from Car.serializers import *
from django.shortcuts import render
from users.views import *
from .serializers import *
# Create your views here.

@api_view(['POST'])
@permission_classes((IsAuthenticated,IsOwnerOrDealer))
def sign_contract(request, industid,dealerid):

    user=request.user
    #   check if a dealer has a permission to sign a contract
    has_perm = user.has_perm('users.can_sign_a_contract') 
    if not (has_perm or user.OWNER):
        return Response(status=status.HTTP_403_FORBIDDEN)

    #   check the existence of such a dealer 
    exists, dealer = check_dealer_exists(dealerid)
    if not exists:
        return Response(status=status.HTTP_404_NOT_FOUND)

     # check if it is an old industry or we should create new one 
    exists, industry = check_industry_exists(industid)
    if not exists:
        serializer = IndustrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    # we create a new object of a contract with all the given data 
    serializer = ContractSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(industry=industry,supervisor=dealer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)