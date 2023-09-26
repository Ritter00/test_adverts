from .models import *
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
       model = City
       fields = ['name',]

      
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
       model = Category
       fields = ['name',]
       
       
class AdvertSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
       model = Advert
       fields = ['id', 'title', 'description', 'created', 'views', 'city', 'category']