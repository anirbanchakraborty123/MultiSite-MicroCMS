from django.contrib import admin
from .models import City,Country,Vendor,Devices,WebPage,PageSection,Lead,Walk_In
# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Vendor)
admin.site.register(Devices)
admin.site.register(WebPage)
admin.site.register(PageSection)
admin.site.register(Lead)
admin.site.register(Walk_In)
