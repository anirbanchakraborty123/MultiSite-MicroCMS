from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class Country(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    status=models.BooleanField(default=True)

class City(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    
class Vendor(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    managedbyuser=models.ForeignKey(User,on_delete=models.CASCADE)
    
class Devices(models.Model):
    device_name=models.CharField(max_length=255,blank=True,null=True)
    device_photo=models.ImageField()
    currency=models.CharField(max_length=255,blank=True,null=True)
    offer_price=models.IntegerField(blank=True,null=True)
    sourced=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    
class Lead(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)
    email_id=models.CharField(max_length=20,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,blank=True,null=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,blank=True,null=True)
    referral_code=models.CharField(max_length=255,blank=True,null=True)
    lead_status=models.CharField(max_length=20,choices=(("Pending","Pending"),
                                          ("In-progress","In-progress"),
                                          ("Converted","Converted"),
                                          ("Rejected","Rejected")),default="Pending")

class Walk_In(models.Model):
    lead=models.ForeignKey(Lead,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    device=models.ForeignKey(Devices,on_delete=models.CASCADE)
    currency=models.CharField(max_length=255,blank=True,null=True)
    offer_price=models.IntegerField(blank=True,null=True)
    walk_in_datetime=models.DateTimeField()
    token_number=models.IntegerField()
    
    def save(self, *args, **kwargs):
        query= Walk_In.objects.all()

        if query.exists() and self._state.adding:
            last_token = query.latest('token_number')
            self.token_number = int(last_token.token_number) + 1
        super().save(*args, **kwargs)
        
class WebPage(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    page_title=models.TextField(blank=True,null=True)
    allowed_devices=models.ForeignKey(Devices,on_delete=models.CASCADE)
    
class PageSection(models.Model):
    section_title=models.TextField(blank=True,null=True)
    section_image=models.ImageField(blank=True,null=True)
    section_HTMLContent=models.TextField(blank=True,null=True)
    section_order=models.IntegerField(blank=True,null=True)
    page=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    active=models.BooleanField(default=1)
    