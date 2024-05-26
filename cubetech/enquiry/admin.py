from django.contrib import admin
from enquiry.models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'address')


admin.site.register(Enquiry,EnquiryAdmin)

# Register your models here.
