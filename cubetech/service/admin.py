from django.contrib import admin
from service.models import Data

class dataAdmin(admin.ModelAdmin):
    list_display=('title', 'description')


admin.site.register(Data,dataAdmin)

# Register your models here.
