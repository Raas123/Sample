from django.contrib import admin
from personal.models import CustomerInfo
from personal.models import OfferInfo
from personal.models import BookedInfo



# Register your models here.
admin.site.register(CustomerInfo)
admin.site.register(OfferInfo)
admin.site.register(BookedInfo)
