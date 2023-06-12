from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import mixins, viewsets,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import Devices,Lead,Vendor,Walk_In,City,Country,WebPage
from .serializers import DevicesSeraializer,LeadSeraializer,Walk_in_Seraializer,WebPageSeraializer
from rest_framework.response import Response
from random import randint
import datetime
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site

    
# To get all the available devices
@api_view(['GET'])
@permission_classes([AllowAny])
def showAllDevices(request):
    if get_current_site(request):
        sites=Site.objects.get(domain=request.get_host())
        if sites:
            try:
                query=WebPage.objects.get(site_id=sites.id)
                serializer=WebPageSeraializer(query)
                return Response(serializer.data)
            except:
                return Response({"error":"No details found"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error":"No details found"},status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"error":"No details found"},status=status.HTTP_204_NO_CONTENT)



# API To generate a token
@api_view(['POST'])
@permission_classes([AllowAny])
def GenerateToken(request):
    if request.method=="POST":
        device=request.data.get('device',None)
        name=request.data.get('name',None)
        phone_no=request.data.get('phone_no',None)
        email_id=request.data.get('email_id',None)
        address=request.data.get('address',None)
        city=request.data.get('city',None)
        country=request.data.get('country',None)
        referral_code=request.data.get('referral_code',None)
        query=Lead.objects.create(name=name,phone_number=phone_no,email_id=email_id,
                                  address=address,city=city,country=country,referral_code=referral_code)
        try:
           check=Country.objects.get(name=country)
        except:
            check=None
        if check and check.status==True:
            devices=Devices.objects.select_related("sourced").filter(device_name=device,sourced__city=City.objects.get(name=city),sourced__country=Country.objects.get(name=country),status=True).values()
            if devices:
                rand = randint(0, devices.count()-1)
                walk_in=Walk_In.objects.create(lead=query,vendor_id=devices[rand]['sourced_id'],device=Devices.objects.get(device_name=device),
                                            currency=devices[rand]['currency'],offer_price=devices[rand]['offer_price'],
                                            walk_in_datetime=datetime.datetime.now()
                                            )
                walk_in.save()
                return Response({"token_number":walk_in.token_number})
            else:
                return Response({"error":"Vendor currently not accepting new walk-ins"},status=status.HTTP_404_NOT_FOUND)
        return Response({"error":"We are currently not serving this country"},status=status.HTTP_404_NOT_FOUND)
