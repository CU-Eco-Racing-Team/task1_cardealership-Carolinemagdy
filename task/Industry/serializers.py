from rest_framework import serializers
from .models import *
# from users.serializers import *

# Serializers define the API representation.
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        extra_kwargs = {'industry': {'read_only': True},'supervisor':{'read_only': True}}

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'

