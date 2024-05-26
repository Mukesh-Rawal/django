from django.db import models

class Data(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
# Create your models here.
