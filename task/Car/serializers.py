from rest_framework import serializers
from .models import *
# from users.serializers import *

# Serializers define the API representation.
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        extra_kwargs = {'industry': {'read_only': True}}

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['price']

