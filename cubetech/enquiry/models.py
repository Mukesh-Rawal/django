from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=50, default='SOME STRING')
    email = models.CharField(max_length=50, default='SOME STRING')
    address = models.CharField(max_length=100 , default='SOME STRING')
# Create your models here.
