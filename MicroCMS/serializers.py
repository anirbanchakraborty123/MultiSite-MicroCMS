from rest_framework import serializers
from .models import Devices,Lead,City,Country,Walk_In,WebPage

class DevicesSeraializer(serializers.ModelSerializer):
    class Meta:
        model=Devices
        fields='__all__'
        depth=1
        
class LeadSeraializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields="__all__"
        depth=1
        
    # def create(self, data):
    #     city, __ = City.objects.get_or_create(city=data["city"])
    #     country,__=Country.objects.get_or_create(country=data["country"])
    #     return Lead(city=city,country=country)
        
class Walk_in_Seraializer(serializers.ModelSerializer):
    class Meta:
        model=Walk_In
        fields="__all__"
        
class WebPageSeraializer(serializers.ModelSerializer):
    class Meta:
        model=WebPage
        fields=["allowed_devices"]
        depth=1

        